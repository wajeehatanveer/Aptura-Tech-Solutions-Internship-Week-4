import time

from automation.ticket_processor import TicketProcessor


def test_ticket_processing_performance():
    processor = TicketProcessor()

    start_time = time.perf_counter()

    result = processor.process_tickets()

    processing_time = time.perf_counter() - start_time

    assert result["total_processed"] >= 0
    assert "tickets" in result
    assert processing_time >= 0

    print(
        f"\nTickets processed: {result['total_processed']}"
    )
    print(
        f"Processing time: {processing_time:.6f} seconds"
    )