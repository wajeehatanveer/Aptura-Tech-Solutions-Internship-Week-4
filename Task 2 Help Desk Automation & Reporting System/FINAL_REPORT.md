# Final Report

## Task 2 — Automation & Quality Engineering

### Project

**Help Desk Automation & Reporting System**

---

## 1. Objective

The objective of this task was to extend the Help Desk Support Ticket Management System with an automated workflow for ticket monitoring, analysis, reporting, scheduling, testing, and performance measurement.

---

## 2. Implementation

The following components were implemented:

* Automated ticket processing
* Priority and ticket-condition analysis
* Unassigned and old-ticket detection
* CSV report generation
* Automation logging
* Scheduled automation
* Processing-time measurement
* Streamlit automation interface
* Unit, integration, and performance testing

The automation workflow analyzes ticket data without automatically modifying or deleting ticket records.

---

## 3. Key Decisions

* Used modular automation components for easier maintenance.
* Used CSV for simple and portable report generation.
* Used SQLite for persistent ticket data.
* Added logging for monitoring and troubleshooting.
* Added automated tests to improve reliability.
* Kept automation read-only to reduce the risk of unintended ticket changes.

---

## 4. Testing & Quality Assurance

The project includes tests for:

* Ticket processing
* Action detection
* CSV report generation
* Scheduler behavior
* Automation integration
* Performance measurement
* Edge cases

All implemented tests passed successfully.

---

## 5. Results

The completed system successfully:

* Processes existing tickets automatically.
* Detects tickets requiring attention.
* Generates timestamped CSV reports.
* Records automation activity.
* Measures processing time.
* Supports scheduled execution.
* Provides a dedicated Streamlit automation interface.

Example generated report:

```text
ticket_automation_report_20260917_003049.csv
```
# 6. Evidence & Screenshots

### Automation Dashboard

The Streamlit automation dashboard demonstrates the automated ticket processing workflow, including the latest run status, processed ticket count, execution timestamp, and generated report status.

![Automation Dashboard](screenshots/Automation-Dashboard.png)

### Run Automation

The automation workflow is executed from the Streamlit dashboard using the **Run Automation Now** option. The system processes the available tickets and identifies tickets requiring attention.

![Automation Running](screenshots/Automation-Run.png)

### Automated Report

The generated automation report displays processed ticket information, including ticket ID, priority, status, assigned staff, and the recommended action for each ticket.

![Automated Report](screenshots/Automation-Report.png)

### Download CSV Report

The generated CSV report is available for download directly from the Streamlit interface, providing a convenient way to save and review the automation results.

![Download CSV Report](screenshots/Automation-Report-Download.png)

---

## 7. Challenges

Some challenges included:

* Converting database rows into structured ticket data.
* Handling invalid or missing ticket dates.
* Designing safe automation rules.
* Integrating report generation with automated processing.
* Testing scheduled workflows without running infinite loops.

These were addressed through validation, exception handling, modular design, and automated testing.

---

## 8. Limitations

* The current automation generates reports but does not send email notifications.
* Scheduled execution requires an external scheduling mechanism for continuous production use.
* Ticket processing is currently based on rule-based conditions.

---

## 9. Future Improvements

Future versions could include:

* Email notifications for critical tickets.
* Advanced ticket prioritization.
* Automated dashboard analytics.
* Database performance optimization.
* Cloud deployment.
* More configurable scheduling options.

---

## 10. Conclusion

The Task 2 implementation successfully extends the Help Desk Support Ticket Management System with automation, reporting, scheduling, testing, logging, and performance monitoring.

The project demonstrates a practical and modular approach to Python automation and quality engineering.

