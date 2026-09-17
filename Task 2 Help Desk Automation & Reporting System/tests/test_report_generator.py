from automation.report_generator import ReportGenerator


def test_generate_csv_report(tmp_path):
    generator = ReportGenerator(
        report_directory=tmp_path
    )

    processing_result = {
        "processed_at": "2026-09-17 00:00:00",
        "total_processed": 1,
        "tickets": [
            {
                "ticket_id": "T001",
                "title": "Unable to login",
                "category": "Technical",
                "priority": "High",
                "status": "Open",
                "assigned_to": "Ahmed",
                "created_at": "2026-09-15 10:00:00",
                "action": "High Priority - Requires Attention"
            }
        ]
    }

    report_path = generator.generate_csv_report(
        processing_result
    )

    assert report_path.exists()
    assert report_path.suffix == ".csv"


def test_generate_empty_report(tmp_path):
    generator = ReportGenerator(
        report_directory=tmp_path
    )

    processing_result = {
        "processed_at": "2026-09-17 00:00:00",
        "total_processed": 0,
        "tickets": []
    }

    report_path = generator.generate_csv_report(
        processing_result
    )

    assert report_path.exists()
    assert report_path.suffix == ".csv"