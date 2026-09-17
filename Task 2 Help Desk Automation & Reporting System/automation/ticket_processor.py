from datetime import datetime, timedelta

from services.ticket_service import TicketService


class TicketProcessor:
    """Automated ticket processing and monitoring."""

    def __init__(self):
        self.ticket_service = TicketService()

    def process_tickets(self):
        """Read and analyze all tickets."""

        tickets = self.ticket_service.get_all_tickets()

        processed_tickets = []

        for ticket in tickets:
            ticket_data = self._convert_ticket(ticket)

            action = self._determine_action(ticket_data)

            ticket_data["action"] = action

            processed_tickets.append(ticket_data)

        return {
            "processed_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "total_processed": len(processed_tickets),
            "tickets": processed_tickets
        }

    def _convert_ticket(self, ticket):
        """Convert SQLite row into a readable dictionary."""

        return {
            "ticket_id": ticket[0],
            "requester_name": ticket[1],
            "email": ticket[2],
            "title": ticket[3],
            "category": ticket[4],
            "priority": ticket[5],
            "description": ticket[6],
            "status": ticket[7],
            "assigned_to": ticket[8],
            "created_at": ticket[9],
            "updated_at": ticket[10],
            "resolved_at": ticket[11]
        }

    def _determine_action(self, ticket):
        """Determine whether a ticket requires attention."""

        status = ticket.get("status", "")
        priority = ticket.get("priority", "")
        assigned_to = ticket.get("assigned_to", "")
        created_at = ticket.get("created_at", "")

        # Resolved or Closed tickets need no further action
        if status in ("Resolved", "Closed"):
            return "No Action Required"

        # Unassigned active tickets
        if (
            not assigned_to
            and status in ("Open", "In Progress")
        ):
            return "Unassigned - Requires Assignment"

        # Critical or High priority active tickets
        if priority in ("Critical", "High"):
            return "High Priority - Requires Attention"

        # In-progress tickets should be monitored
        if status == "In Progress":
            return "In Progress - Requires Monitoring"

        # Old open tickets
        if (
            status == "Open"
            and self._is_old_ticket(created_at)
        ):
            return "Old Open Ticket - Requires Attention"

        return "No Immediate Action Required"

    def _is_old_ticket(self, created_at, days=2):
        """Check whether a ticket is older than the given days."""

        if not created_at:
            return False

        try:
            created_time = datetime.strptime(
                created_at,
                "%Y-%m-%d %H:%M:%S"
            )

            threshold = datetime.now() - timedelta(days=days)

            return created_time < threshold

        except (ValueError, TypeError):
            return False