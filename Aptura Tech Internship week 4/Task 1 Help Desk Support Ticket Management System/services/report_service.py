class ReportService:

    def __init__(self, ticket_service):
        self.ticket_service = ticket_service

    def get_ticket_summary(self):
        tickets = self.ticket_service.get_all_tickets()

        summary = {
            "total": len(tickets),
            "open": 0,
            "in_progress": 0,
            "resolved": 0,
            "closed": 0,
            "high_priority": 0,
            "critical_priority": 0
        }

        for ticket in tickets:
            status = ticket[7].lower()
            priority = ticket[5].lower()

            if status == "open":
                summary["open"] += 1

            elif status == "in progress":
                summary["in_progress"] += 1

            elif status == "resolved":
                summary["resolved"] += 1

            elif status == "closed":
                summary["closed"] += 1

            if priority == "high":
                summary["high_priority"] += 1

            elif priority == "critical":
                summary["critical_priority"] += 1

        return summary

    def get_category_report(self):
        tickets = self.ticket_service.get_all_tickets()
        category_report = {}

        for ticket in tickets:
            category = ticket[4]

            if category not in category_report:
                category_report[category] = 0

            category_report[category] += 1

        return category_report

    def get_priority_report(self):
        tickets = self.ticket_service.get_all_tickets()
        priority_report = {}

        for ticket in tickets:
            priority = ticket[5]

            if priority not in priority_report:
                priority_report[priority] = 0

            priority_report[priority] += 1

        return priority_report

    def get_status_report(self):
        tickets = self.ticket_service.get_all_tickets()
        status_report = {}

        for ticket in tickets:
            status = ticket[7]

            if status not in status_report:
                status_report[status] = 0

            status_report[status] += 1

        return status_report