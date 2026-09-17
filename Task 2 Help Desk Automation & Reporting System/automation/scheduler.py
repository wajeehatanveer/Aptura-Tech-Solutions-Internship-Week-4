import time
from datetime import datetime

from automation.ticket_processor import TicketProcessor
from automation.report_generator import ReportGenerator
from utils.logger import logger


class AutomationScheduler:
    """Run ticket automation on a scheduled interval."""

    def __init__(self, interval_minutes=60):
        self.interval_seconds = interval_minutes * 60

        self.processor = TicketProcessor()
        self.report_generator = ReportGenerator()

    def run_once(self):
        """Run the automation workflow once."""

        start_time = datetime.now()

        try:
            logger.info("Starting automated ticket processing.")

            processing_result = self.processor.process_tickets()

            report_path = self.report_generator.generate_csv_report(
                processing_result
            )

            end_time = datetime.now()
            processing_time = (
                end_time - start_time
            ).total_seconds()

            logger.info(
                "Automation completed successfully. "
                f"Tickets processed: "
                f"{processing_result['total_processed']}. "
                f"Processing time: "
                f"{processing_time:.2f} seconds. "
                f"Report: {report_path}"
            )

            return {
                "processed_at": processing_result["processed_at"],
                "total_processed": processing_result["total_processed"],
                "processing_time": processing_time,
                "report_path": report_path
            }

        except Exception as error:
            logger.exception(
                f"Automation failed: {error}"
            )

            raise RuntimeError(
                "Automated ticket processing failed."
            ) from error

    def run_continuously(self):
        """Run automation repeatedly at the configured interval."""

        logger.info(
            "Scheduled automation started. "
            f"Interval: {self.interval_seconds // 60} minutes."
        )

        while True:
            self.run_once()

            logger.info(
                "Waiting for the next scheduled run."
            )

            time.sleep(self.interval_seconds)