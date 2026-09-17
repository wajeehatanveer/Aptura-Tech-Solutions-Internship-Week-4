from automation.ticket_processor import TicketProcessor
from automation.report_generator import ReportGenerator


def test_automation_workflow_integration(tmp_path):
    processor = TicketProcessor()

    processing_result = processor.process_tickets()

    generator = ReportGenerator(
        report_directory=tmp_path
    )

    report_path = generator.generate_csv_report(
        processing_result
    )

    assert processing_result["total_processed"] >= 0
    assert "tickets" in processing_result

    assert report_path.exists()
    assert report_path.suffix == ".csv"