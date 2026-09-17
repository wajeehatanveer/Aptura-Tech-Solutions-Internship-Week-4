import csv
from datetime import datetime
from pathlib import Path

from utils.logger import logger


class ReportGenerator:
    """Generate automated ticket reports."""

    def __init__(self, report_directory="reports"):
        self.report_directory = Path(report_directory)
        self.report_directory.mkdir(
            parents=True,
            exist_ok=True
        )

    def generate_csv_report(self, processing_result):
        """Generate a CSV report from processed ticket data."""

        try:
            tickets = processing_result.get("tickets", [])

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            report_path = (
                self.report_directory
                / f"ticket_automation_report_{timestamp}.csv"
            )

            with report_path.open(
                mode="w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Ticket ID",
                    "Title",
                    "Category",
                    "Priority",
                    "Status",
                    "Assigned To",
                    "Created At",
                    "Action"
                ])

                for ticket in tickets:
                    writer.writerow([
                        ticket.get("ticket_id", ""),
                        ticket.get("title", ""),
                        ticket.get("category", ""),
                        ticket.get("priority", ""),
                        ticket.get("status", ""),
                        ticket.get("assigned_to", ""),
                        ticket.get("created_at", ""),
                        ticket.get("action", "")
                    ])

            logger.info(
                f"Automation report generated: {report_path}"
            )

            return report_path

        except (OSError, csv.Error) as error:
            logger.exception(
                f"Failed to generate automation report: {error}"
            )

            raise RuntimeError(
                "Unable to generate the automation report."
            )