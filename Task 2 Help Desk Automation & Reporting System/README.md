## Aptura Tech Solutions — Python Internship | Week 4

### Task 2 — Automation & Quality Engineering

## Help Desk Automation & Reporting System

An automation and quality engineering extension of the Help Desk Support Ticket Management System.

The system automatically processes ticket data, identifies tickets that may require attention, generates CSV reports, records automation activity, measures processing time, and supports scheduled execution.

The automation workflow is designed as a safe monitoring and reporting process and does not automatically modify or delete ticket records.

---

## Features

* Automated ticket processing
* High and Critical priority detection
* Unassigned ticket detection
* Old open ticket detection
* Automated CSV report generation
* Timestamped reports
* Automation execution logging
* Processing-time measurement
* Scheduled automation support
* Unit testing
* Integration testing
* Performance testing
* Edge-case handling
* Streamlit automation dashboard

---

## Automation Workflow

```text
SQLite Database
       ↓
Ticket Processor
       ↓
Ticket Analysis
       ↓
Action Detection
       ↓
Report Generator
       ↓
CSV Report
       ↓
Logs
```

---

## Project Structure

```text
Task 2 - Help Desk Automation & Reporting System/
## Project Structure

```text
Help Desk Automation & Reporting System/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── RUNBOOK.md
├── FINAL_REPORT.md
│
├── automation/
│   ├── __init__.py
│   ├── ticket_processor.py
│   ├── report_generator.py
│   └── scheduler.py
│
├── database/
│   ├── __init__.py
│   └── database.py
│
├── models/
│   ├── __init__.py
│   ├── ticket.py
│   └── staff.py
│
├── services/
│   ├── __init__.py
│   ├── ticket_service.py
│   ├── staff_service.py
│   └── report_service.py
│
├── utils/
│   ├── __init__.py
│   ├── validation.py
│   └── logger.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_automation.py
│   ├── test_report_generator.py
│   ├── test_scheduler.py
│   ├── test_automation_integration.py
│   └── test_performance.py
│
├── data/
│
├── logs/
│
├── reports/
│   └── ticket_automation_report_YYYYMMDD_HHMMSS.csv
│
└── screenshots/
    ├── Automation-Dashboard.png
    ├── Automation-Run.png
    ├── Automation-Report.png
    └── Automation-Report-Download.png
    ├── Dashboard_Overview.png
    ├── Dashboard_Overview.png
    ├── New_Ticket.png
    ├── Ticket_created_successfully.png
    ├── Ticket_Management.png
    ├── Ticket_History.png
    ├── Delete_Ticket.png
    ├── Add_Staff_Member.png
    ├── Staff_Records.png
    ├── Delete_Staff.png
    ├── Reports_And_Analytics.png
    └── Report.png

```

## How Automation Works

When automation is executed, the system:

1. Reads ticket records from SQLite.
2. Converts ticket data into a structured format.
3. Analyzes ticket priority, status, assignment, and age.
4. Identifies tickets requiring attention.
5. Generates a timestamped CSV report.
6. Records automation activity in the logs.
7. Measures processing time.

Example actions:

```text
High Priority - Requires Attention

Unassigned - Requires Assignment

Old Open Ticket - Requires Attention

No Immediate Action Required
```

---

## Running the Application

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the **Automation** page and select:

**Run Automation Now**

The latest automation run and generated report are displayed in the dashboard.

---

## Automated Reports

Generated reports are stored in:

```text
reports/
```

Example:

```text
ticket_automation_report_20260917_003049.csv
```


---

## Testing

Run the complete test suite:

```bash
pytest tests -v
```

All implemented tests pass successfully.

Run the performance test separately:

```bash
pytest tests/test_performance.py -v -s
```

---

## Scheduling

The project includes an `AutomationScheduler` for repeated automated processing.

Example:

```python
from automation.scheduler import AutomationScheduler

scheduler = AutomationScheduler(
    interval_minutes=60
)

scheduler.run_continuously()
```

The scheduler can be connected to an operating-system scheduling service for production deployment.

---

## Logging

Automation events, report generation, successful executions, and errors are recorded using the application's logging system.

Logs are stored in:

```text
logs/
```

---

## Safe Automation

The automation workflow is intentionally read-only with respect to ticket records.

It does not automatically:

* Delete tickets
* Modify ticket status
* Change ticket priority
* Reassign tickets

This helps prevent unintended changes to operational data.

---

## Documentation

Additional project documentation:

* `RUNBOOK.md` — deployment, operation, testing, and troubleshooting
* `FINAL_REPORT.md` — Task 2 decisions, implementation, results, limitations, and future improvements

---

## Technology Stack

* Python
* Streamlit
* SQLite
* Pytest
* CSV
* Python Logging
* Object-Oriented Programming
* Modular Architecture

---

## Project Outcome

This project extends the original Help Desk Support Ticket Management System with an automated workflow for ticket monitoring and reporting.

The implementation demonstrates:

* Automation
* Modular Python development
* Validation and error handling
* Persistent data processing
* Automated reporting
* Logging
* Scheduling
* Testing and quality assurance
* Performance measurement
* Professional documentation

## Internship Task

 Organization: Aptura Tech Solutions
 Internship: Python Internship
 Week: 4
 Task: Task 2 — Automation & Quality Engineering