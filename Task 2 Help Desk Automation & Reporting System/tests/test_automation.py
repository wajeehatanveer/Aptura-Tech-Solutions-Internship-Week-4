from datetime import datetime, timedelta

from automation.ticket_processor import TicketProcessor


def create_ticket(
    ticket_id="T001",
    title="Test Ticket",
    priority="Medium",
    status="Open",
    assigned_to="Ahmed",
    created_at=None
):
    """Create a test ticket in database-row format."""

    if created_at is None:
        created_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    return (
        ticket_id,
        "Test User",
        "test@example.com",
        title,
        "Technical",
        priority,
        "Test description",
        status,
        assigned_to,
        created_at,
        created_at,
        ""
    )


def test_convert_ticket():
    processor = TicketProcessor()

    ticket = create_ticket()

    result = processor._convert_ticket(ticket)

    assert result["ticket_id"] == "T001"
    assert result["title"] == "Test Ticket"
    assert result["priority"] == "Medium"
    assert result["status"] == "Open"
    assert result["assigned_to"] == "Ahmed"


def test_critical_ticket_requires_attention():
    processor = TicketProcessor()

    ticket = {
        "priority": "Critical",
        "status": "Open",
        "assigned_to": "Ahmed",
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    result = processor._determine_action(ticket)

    assert result == "High Priority - Requires Attention"


def test_high_priority_ticket_requires_attention():
    processor = TicketProcessor()

    ticket = {
        "priority": "High",
        "status": "Open",
        "assigned_to": "Ahmed",
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    result = processor._determine_action(ticket)

    assert result == "High Priority - Requires Attention"


def test_unassigned_ticket_requires_assignment():
    processor = TicketProcessor()

    ticket = {
        "priority": "Medium",
        "status": "Open",
        "assigned_to": "",
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    result = processor._determine_action(ticket)

    assert result == "Unassigned - Requires Assignment"


def test_old_open_ticket_requires_attention():
    processor = TicketProcessor()

    old_date = (
        datetime.now() - timedelta(days=3)
    ).strftime("%Y-%m-%d %H:%M:%S")

    ticket = {
        "priority": "Medium",
        "status": "Open",
        "assigned_to": "Ahmed",
        "created_at": old_date
    }

    result = processor._determine_action(ticket)

    assert result == "Old Open Ticket - Requires Attention"


def test_resolved_old_ticket_does_not_require_attention():
    processor = TicketProcessor()

    old_date = (
        datetime.now() - timedelta(days=5)
    ).strftime("%Y-%m-%d %H:%M:%S")

    ticket = {
        "priority": "Medium",
        "status": "Resolved",
        "assigned_to": "Ahmed",
        "created_at": old_date
    }

    result = processor._determine_action(ticket)

    assert result == "No Immediate Action Required"


def test_normal_ticket_requires_no_immediate_action():
    processor = TicketProcessor()

    ticket = {
        "priority": "Low",
        "status": "Open",
        "assigned_to": "Ahmed",
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    result = processor._determine_action(ticket)

    assert result == "No Immediate Action Required"


def test_empty_created_at_is_handled():
    processor = TicketProcessor()

    result = processor._is_old_ticket("")

    assert result is False


def test_invalid_created_at_is_handled():
    processor = TicketProcessor()

    result = processor._is_old_ticket(
        "invalid-date"
    )

    assert result is False