import sqlite3
from pathlib import Path

DATABASE_PATH = Path("data/helpdesk.db")


def get_connection():
    DATABASE_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id TEXT PRIMARY KEY,
            requester_name TEXT NOT NULL,
            email TEXT NOT NULL,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            priority TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL,
            assigned_to TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            resolved_at TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS staff (
            staff_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            department TEXT NOT NULL,
            role TEXT NOT NULL,
            availability TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ticket_updates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id TEXT NOT NULL,
            update_type TEXT NOT NULL,
            details TEXT,
            updated_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()