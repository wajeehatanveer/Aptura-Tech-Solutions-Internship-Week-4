import pytest

from database.database import initialize_database
from models.ticket import Ticket
from services.ticket_service import TicketService


@pytest.fixture
def ticket_service(tmp_path, monkeypatch):
    """
    Create an isolated temporary database for testing.
    """

    import database.database as database_module

    test_database = tmp_path / "test_helpdesk.db"

    monkeypatch.setattr(
        database_module,
        "DATABASE_PATH",
        test_database
    )

    initialize_database()

    return TicketService()


@pytest.fixture
def sample_ticket():
    return Ticket(
        ticket_id="",
        requester_name="Test User",
        email="test@example.com",
        title="Login Problem",
        category="Software",
        priority="High",
        description="Unable to login to the system.",
        status="Open"
    )


def test_create_ticket(ticket_service, sample_ticket):

    created_ticket = ticket_service.create_ticket(
        sample_ticket
    )

    assert created_ticket.ticket_id == "T001"
    assert created_ticket.requester_name == "Test User"
    assert created_ticket.status == "Open"


def test_get_ticket(ticket_service, sample_ticket):

    created_ticket = ticket_service.create_ticket(
        sample_ticket
    )

    ticket = ticket_service.get_ticket(
        created_ticket.ticket_id
    )

    assert ticket is not None
    assert ticket[0] == "T001"
    assert ticket[1] == "Test User"
    assert ticket[3] == "Login Problem"


def test_get_all_tickets(ticket_service, sample_ticket):

    ticket_service.create_ticket(sample_ticket)

    tickets = ticket_service.get_all_tickets()

    assert len(tickets) == 1


def test_search_tickets(ticket_service, sample_ticket):

    ticket_service.create_ticket(sample_ticket)

    results = ticket_service.search_tickets(
        "Login"
    )

    assert len(results) == 1
    assert results[0][3] == "Login Problem"


def test_update_ticket(ticket_service, sample_ticket):

    created_ticket = ticket_service.create_ticket(
        sample_ticket
    )

    result = ticket_service.update_ticket(
        created_ticket.ticket_id,
        status="In Progress",
        priority="Critical",
        assigned_to="S001",
        resolution_note="Issue is being investigated."
    )

    assert result is True

    updated_ticket = ticket_service.get_ticket(
        created_ticket.ticket_id
    )

    assert updated_ticket[5] == "Critical"
    assert updated_ticket[7] == "In Progress"
    assert updated_ticket[8] == "S001"


def test_ticket_history(ticket_service, sample_ticket):

    created_ticket = ticket_service.create_ticket(
        sample_ticket
    )

    ticket_service.update_ticket(
        created_ticket.ticket_id,
        status="Resolved",
        resolution_note="Issue resolved successfully."
    )

    updates = ticket_service.get_ticket_updates(
        created_ticket.ticket_id
    )

    assert len(updates) == 2


def test_delete_ticket(ticket_service, sample_ticket):

    created_ticket = ticket_service.create_ticket(
        sample_ticket
    )

    result = ticket_service.delete_ticket(
        created_ticket.ticket_id
    )

    assert result is True

    ticket = ticket_service.get_ticket(
        created_ticket.ticket_id
    )

    assert ticket is None


def test_update_nonexistent_ticket(ticket_service):

    result = ticket_service.update_ticket(
        "T999",
        status="Resolved"
    )

    assert result is False


def test_delete_nonexistent_ticket(ticket_service):

    result = ticket_service.delete_ticket(
        "T999"
    )

    assert result is False