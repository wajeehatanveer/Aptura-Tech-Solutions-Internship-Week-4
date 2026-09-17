from utils.validation import (
    validate_required,
    validate_email,
    validate_priority,
    validate_category,
    validate_status,
    validate_ticket_data
)


CATEGORIES = [
    "Network",
    "Software",
    "Hardware",
    "Account",
    "Email",
    "Other"
]

PRIORITIES = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

STATUSES = [
    "Open",
    "In Progress",
    "Resolved",
    "Closed"
]


def test_required_field_valid():
    valid, message = validate_required(
        "Wajeeha",
        "Requester name"
    )

    assert valid is True
    assert message == ""


def test_required_field_empty():
    valid, message = validate_required(
        "",
        "Requester name"
    )

    assert valid is False
    assert "required" in message.lower()


def test_valid_email():
    valid, message = validate_email(
        "user@example.com"
    )

    assert valid is True
    assert message == ""


def test_invalid_email():
    valid, message = validate_email(
        "invalid-email"
    )

    assert valid is False
    assert "valid email" in message.lower()


def test_valid_priority():
    valid, message = validate_priority(
        "High",
        PRIORITIES
    )

    assert valid is True


def test_invalid_priority():
    valid, message = validate_priority(
        "Urgent",
        PRIORITIES
    )

    assert valid is False


def test_valid_category():
    valid, message = validate_category(
        "Software",
        CATEGORIES
    )

    assert valid is True


def test_invalid_category():
    valid, message = validate_category(
        "Unknown",
        CATEGORIES
    )

    assert valid is False


def test_valid_status():
    valid, message = validate_status(
        "Open",
        STATUSES
    )

    assert valid is True


def test_invalid_status():
    valid, message = validate_status(
        "Pending",
        STATUSES
    )

    assert valid is False


def test_complete_valid_ticket_data():
    valid, message = validate_ticket_data(
        "Wajeeha Tanveer",
        "wajeeha@example.com",
        "Login Problem",
        "Software",
        "High",
        "Unable to login to the system.",
        CATEGORIES,
        PRIORITIES
    )

    assert valid is True
    assert message == "Validation successful."


def test_complete_invalid_ticket_data():
    valid, message = validate_ticket_data(
        "Wajeeha Tanveer",
        "invalid-email",
        "Login Problem",
        "Software",
        "High",
        "Unable to login to the system.",
        CATEGORIES,
        PRIORITIES
    )

    assert valid is False