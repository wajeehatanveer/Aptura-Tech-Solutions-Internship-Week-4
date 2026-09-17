import pytest

from database.database import initialize_database
from models.ticket import Ticket
from services.ticket_service import TicketService
from services.report_service import ReportService


@pytest.fixture
def report_service(tmp_path, monkeypatch):

    import database.database as database_module

    test_database = tmp_path / "test_helpdesk.db"

    monkeypatch.setattr(
        database_module,
        "DATABASE_PATH",
        test_database
    )

    initialize_database()

    ticket_service = TicketService()

    return ReportService(ticket_service)


@pytest.fixture
def ticket_service(tmp_path, monkeypatch):

    import database.database as database_module

    test_database = tmp_path / "test_helpdesk.db"

    monkeypatch.setattr(
        database_module,
        "DATABASE_PATH",
        test_database
    )

    initialize_database()

    return TicketService()


def create_sample_ticket(
    ticket_service,
    title,
    category,
    priority,
    status
):
    ticket = Ticket(
        ticket_id="",
        requester_name="Test User",
        email="test@example.com",
        title=title,
        category=category,
        priority=priority,
        description="Test ticket description.",
        status=status
    )

    return ticket_service.create_ticket(ticket)


def test_ticket_summary(report_service, ticket_service):

    create_sample_ticket(
        ticket_service,
        "Login Issue",
        "Software",
        "High",
        "Open"
    )

    create_sample_ticket(
        ticket_service,
        "Network Issue",
        "Network",
        "Critical",
        "In Progress"
    )

    create_sample_ticket(
        ticket_service,
        "Hardware Issue",
        "Hardware",
        "Low",
        "Resolved"
    )

    summary = report_service.get_ticket_summary()

    assert summary["total"] == 3
    assert summary["open"] == 1
    assert summary["in_progress"] == 1
    assert summary["resolved"] == 1
    assert summary["closed"] == 0
    assert summary["high_priority"] == 1
    assert summary["critical_priority"] == 1


def test_category_report(report_service, ticket_service):

    create_sample_ticket(
        ticket_service,
        "Login Issue",
        "Software",
        "High",
        "Open"
    )

    create_sample_ticket(
        ticket_service,
        "Application Error",
        "Software",
        "Medium",
        "Open"
    )

    create_sample_ticket(
        ticket_service,
        "Network Issue",
        "Network",
        "Critical",
        "In Progress"
    )

    category_report = report_service.get_category_report()

    assert category_report["Software"] == 2
    assert category_report["Network"] == 1


def test_priority_report(report_service, ticket_service):

    create_sample_ticket(
        ticket_service,
        "High Priority Issue",
        "Software",
        "High",
        "Open"
    )

    create_sample_ticket(
        ticket_service,
        "Critical Issue",
        "Network",
        "Critical",
        "Open"
    )

    create_sample_ticket(
        ticket_service,
        "Low Priority Issue",
        "Hardware",
        "Low",
        "Resolved"
    )

    priority_report = report_service.get_priority_report()

    assert priority_report["High"] == 1
    assert priority_report["Critical"] == 1
    assert priority_report["Low"] == 1


def test_status_report(report_service, ticket_service):

    create_sample_ticket(
        ticket_service,
        "Open Issue",
        "Software",
        "Medium",
        "Open"
    )

    create_sample_ticket(
        ticket_service,
        "Progress Issue",
        "Network",
        "High",
        "In Progress"
    )

    create_sample_ticket(
        ticket_service,
        "Resolved Issue",
        "Hardware",
        "Low",
        "Resolved"
    )

    create_sample_ticket(
        ticket_service,
        "Closed Issue",
        "Account",
        "Medium",
        "Closed"
    )

    status_report = report_service.get_status_report()

    assert status_report["Open"] == 1
    assert status_report["In Progress"] == 1
    assert status_report["Resolved"] == 1
    assert status_report["Closed"] == 1