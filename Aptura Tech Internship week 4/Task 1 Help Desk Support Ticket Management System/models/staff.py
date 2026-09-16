from dataclasses import dataclass


@dataclass
class Staff:
    staff_id: str
    name: str
    email: str
    department: str
    role: str
    availability: str = "Available"