from automation.scheduler import AutomationScheduler


def test_scheduler_interval():
    scheduler = AutomationScheduler(
        interval_minutes=30
    )

    assert scheduler.interval_seconds == 1800


def test_scheduler_run_once(monkeypatch, tmp_path):
    scheduler = AutomationScheduler(
        interval_minutes=30
    )

    scheduler.report_generator.report_directory = tmp_path

    processing_result = {
        "processed_at": "2026-09-17 00:00:00",
        "total_processed": 2,
        "tickets": []
    }

    monkeypatch.setattr(
        scheduler.processor,
        "process_tickets",
        lambda: processing_result
    )

    result = scheduler.run_once()

    assert result["total_processed"] == 2
    assert result["processing_time"] >= 0
    assert result["report_path"].exists()