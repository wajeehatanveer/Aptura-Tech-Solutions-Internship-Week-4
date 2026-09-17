from dataclasses import dataclass


@dataclass
class Ticket:
    ticket_id: str
    requester_name: str
    email: str
    title: str
    category: str
    priority: str
    description: str
    status: str = "Open"
    assigned_to: str = ""
    created_at: str = ""
    updated_at: str = ""
    resolved_at: str = ""