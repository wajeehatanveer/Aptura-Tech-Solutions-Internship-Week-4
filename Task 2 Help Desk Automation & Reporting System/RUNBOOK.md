# Deployment & Runbook

## 1. Project Overview

The **Help Desk Automation & Reporting System** extends the Help Desk Support Ticket Management System with automated ticket processing, monitoring, reporting, scheduling, testing, and performance measurement.

The automation analyzes ticket data and generates reports without modifying or deleting ticket records.

---

## 2. Requirements

* Python 3.10+
* Streamlit
* SQLite
* pytest

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 3. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the **Automation** page and click:

**Run Automation Now**

The system will:

1. Read ticket data.
2. Analyze tickets.
3. Identify tickets requiring attention.
4. Generate a CSV report.
5. Record the automation result and processing time.

---

## 4. Automated Reports

Generated reports are stored in:

```text
reports/
```

Example:

```text
ticket_automation_report_20260917_003049.csv
```

The report contains:

* Ticket ID
* Title
* Category
* Priority
* Status
* Assigned To
* Created At
* Action

---

## 5. Scheduled Automation

The project includes an `AutomationScheduler` for running the automation workflow at a configured interval.

Example:

```python
from automation.scheduler import AutomationScheduler

scheduler = AutomationScheduler(interval_minutes=60)

scheduler.run_continuously()
```

The scheduler can be integrated with **Windows Task Scheduler** or **Linux cron** for automated execution.

---

## 6. Testing

Run the complete test suite:

```bash
pytest tests -v
```

The test suite covers:

* Ticket processing
* Action detection
* CSV report generation
* Scheduler functionality
* Integration workflow
* Edge cases
* Performance testing

Run the performance test:

```bash
pytest tests/test_performance.py -v -s
```

All implemented tests were successfully executed during project validation.

---

## 7. Logging

Automation events, execution details, and errors are recorded through the application logging system.

Logs are stored in:

```text
logs/
```

---

## 8. Troubleshooting

### Application Does Not Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Tests Fail

```bash
pytest tests -v
```

Review the failed test and check the related module.

### Report Is Not Generated

Check the `reports/` directory and review the application logs for errors.

---

## 9. Deployment Checklist

* [ ] Install dependencies
* [ ] Run all tests
* [ ] Run performance test
* [ ] Start Streamlit application
* [ ] Run automation
* [ ] Verify generated CSV report
* [ ] Verify logs
* [ ] Verify scheduler configuration

---

## 10. Safe Automation

The automation is designed for monitoring and reporting.

It does not automatically:

* Delete tickets
* Modify ticket status
* Change priority
* Reassign tickets

This ensures that automated processing does not unintentionally change or remove help desk records.
