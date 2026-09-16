## Aptura Tech Solutions — Python Internship

### Week 4 — Task 1 — Production-Grade Python Application

# Help Desk / Support Ticket Management System

## Project Overview

The Help Desk / Support Ticket Management System is a Python-based application developed as part of the Aptura Tech Solutions Python Internship — Week 4 Task 1.

The system is designed to manage support tickets, staff assignments, ticket updates, and reports through a structured and user-friendly interface.

## Key Features

- Create and manage support tickets
- View and update ticket information
- Assign tickets to staff members
- Manage staff records
- Track ticket status and updates
- Generate reports
- Persistent data storage using SQLite
- Input validation
- Exception handling
- Application logging
- Automated testing
- Modular project architecture
- Streamlit-based user interface

## Project Structure

```text
HelpDesk-Support-Ticket-Management-System/
│
├── app.py
├── config.py
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
│── Screenshots/
│
├── 1- Dashboard_Overview.png
├── 2- Dashboard_Overview.png
├── 3- New_Ticket.png
├── 4- Ticket_created_successfully.png
├── 5- Ticket_Management.png
├── 6- Ticket_History.png
├── 7- Delete_Ticket.png
├── 8- Add_Staff_Member.png
├── 9- Staff_Records.png
├── 10- Delete_Staff.png
├── 11- Reports_And_Analytics.png
└── 12- Report.png
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
│   ├── conftest.py
│   ├── test_validation.py
│   ├── test_ticket.py
│   ├── test_staff.py
│   └── test_reports.py
│
├── data/
├── logs/
├── requirements.txt
└── README.md
````

## Application Modules

### Dashboard

Provides an overview of the help desk system and its ticket-related information.

### New Ticket

Allows users to create new support tickets by entering requester and issue details.

### Tickets

Provides ticket management functionality, including viewing and updating tickets.

### Staff

Allows staff records to be managed and tickets to be assigned to staff members.

### Reports

Provides report-related information based on the stored ticket data.

## Database

The application uses **SQLite** for persistent data storage.

The database contains tables for:

* Tickets
* Staff
* Ticket Updates

This allows ticket information and ticket history to remain stored between application sessions.

## Validation

Input validation is implemented to ensure that required information is properly entered and invalid data is handled safely.

## Logging & Exception Handling

The application includes logging and exception handling to make errors easier to identify and prevent unexpected application failures.

Database operations also use safe connection handling and rollback mechanisms when required.

## Testing

The project includes automated tests using **pytest**.

Test files cover:

* Validation
* Ticket functionality
* Staff functionality
* Reports

### Test Result

All project tests passed successfully.

**34 / 34 tests passed**

## Technologies Used

* Python
* Streamlit
* SQLite
* Pytest
* Dataclasses
* Logging

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit application

```bash
streamlit run app.py
```

### 3. Run the tests

```bash
pytest -v
```

## Conclusion

This project demonstrates the implementation of a modular Python application with persistent storage, validation, logging, exception handling, reporting, a Streamlit interface, and automated testing.

```
## Internship Task

**Organization:** Aptura Tech Solutions
**Internship:** Python Internship
**Week:** 4
**Task:** Task 1 — Help Desk / Support Ticket Management System