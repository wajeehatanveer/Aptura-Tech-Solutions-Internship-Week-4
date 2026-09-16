import re


def validate_required(value, field_name):
    if not value or not str(value).strip():
        return False, f"{field_name} is required."

    return True, ""


def validate_email(email):
    if not email or not email.strip():
        return False, "Email is required."

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        return False, "Please enter a valid email address."

    return True, ""


def validate_priority(priority, allowed_priorities):
    if priority not in allowed_priorities:
        return False, "Please select a valid priority."

    return True, ""


def validate_category(category, allowed_categories):
    if category not in allowed_categories:
        return False, "Please select a valid category."

    return True, ""


def validate_status(status, allowed_statuses):
    if status not in allowed_statuses:
        return False, "Please select a valid status."

    return True, ""


def validate_ticket_data(
    requester_name,
    email,
    title,
    category,
    priority,
    description,
    allowed_categories,
    allowed_priorities
):
    fields = [
        (requester_name, "Requester name"),
        (title, "Issue title"),
        (description, "Description")
    ]

    for value, field_name in fields:
        valid, message = validate_required(value, field_name)

        if not valid:
            return False, message

    valid, message = validate_email(email)

    if not valid:
        return False, message

    valid, message = validate_category(
        category,
        allowed_categories
    )

    if not valid:
        return False, message

    valid, message = validate_priority(
        priority,
        allowed_priorities
    )

    if not valid:
        return False, message

    return True, "Validation successful."