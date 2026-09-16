# from datetime import datetime

# from database.database import get_connection
# from models.ticket import Ticket
# from utils.logger import logger


# class TicketService:

#     def generate_ticket_id(self):
#         connection = get_connection()
#         cursor = connection.cursor()

#         cursor.execute(
#             "SELECT ticket_id FROM tickets ORDER BY rowid DESC LIMIT 1"
#         )

#         result = cursor.fetchone()

#         connection.close()

#         if result:
#             number = int(result[0][1:]) + 1
#         else:
#             number = 1

#         return f"T{number:03d}"

#     def create_ticket(self, ticket):
#         connection = get_connection()
#         cursor = connection.cursor()

#         now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         ticket.ticket_id = self.generate_ticket_id()
#         ticket.created_at = now
#         ticket.updated_at = now

#         cursor.execute("""
#             INSERT INTO tickets (
#                 ticket_id,
#                 requester_name,
#                 email,
#                 title,
#                 category,
#                 priority,
#                 description,
#                 status,
#                 assigned_to,
#                 created_at,
#                 updated_at,
#                 resolved_at
#             )
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#         """, (
#             ticket.ticket_id,
#             ticket.requester_name,
#             ticket.email,
#             ticket.title,
#             ticket.category,
#             ticket.priority,
#             ticket.description,
#             ticket.status,
#             ticket.assigned_to,
#             ticket.created_at,
#             ticket.updated_at,
#             ticket.resolved_at
#         ))

#         connection.commit()
#         connection.close()

#         logger.info(
#             f"Ticket created successfully: {ticket.ticket_id}"
#         )

#         return ticket

#     def get_all_tickets(self):
#         connection = get_connection()
#         cursor = connection.cursor()

#         cursor.execute(
#             "SELECT * FROM tickets ORDER BY rowid DESC"
#         )

#         rows = cursor.fetchall()

#         connection.close()

#         return rows

#     def get_ticket(self, ticket_id):
#         connection = get_connection()
#         cursor = connection.cursor()

#         cursor.execute(
#             "SELECT * FROM tickets WHERE ticket_id = ?",
#             (ticket_id,)
#         )

#         ticket = cursor.fetchone()

#         connection.close()

#         return ticket

#     def search_tickets(self, keyword):
#         connection = get_connection()
#         cursor = connection.cursor()

#         keyword = f"%{keyword}%"

#         cursor.execute("""
#             SELECT * FROM tickets
#             WHERE ticket_id LIKE ?
#                OR requester_name LIKE ?
#                OR title LIKE ?
#         """, (
#             keyword,
#             keyword,
#             keyword
#         ))

#         results = cursor.fetchall()

#         connection.close()

#         return results

#     def update_ticket(
#         self,
#         ticket_id,
#         status=None,
#         priority=None,
#         assigned_to=None,
#         resolution_note=None
#     ):
#         connection = get_connection()
#         cursor = connection.cursor()

#         now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         cursor.execute("""
#             UPDATE tickets
#             SET status = COALESCE(?, status),
#                 priority = COALESCE(?, priority),
#                 assigned_to = COALESCE(?, assigned_to),
#                 updated_at = ?
#             WHERE ticket_id = ?
#         """, (
#             status,
#             priority,
#             assigned_to,
#             now,
#             ticket_id
#         ))

#         if status:
#             cursor.execute("""
#                 INSERT INTO ticket_updates (
#                     ticket_id,
#                     update_type,
#                     details,
#                     updated_at
#                 )
#                 VALUES (?, ?, ?, ?)
#             """, (
#                 ticket_id,
#                 "Status Changed",
#                 status,
#                 now
#             ))

#         if priority:
#             cursor.execute("""
#                 INSERT INTO ticket_updates (
#                     ticket_id,
#                     update_type,
#                     details,
#                     updated_at
#                 )
#                 VALUES (?, ?, ?, ?)
#             """, (
#                 ticket_id,
#                 "Priority Changed",
#                 priority,
#                 now
#             ))

#         if assigned_to:
#             cursor.execute("""
#                 INSERT INTO ticket_updates (
#                     ticket_id,
#                     update_type,
#                     details,
#                     updated_at
#                 )
#                 VALUES (?, ?, ?, ?)
#             """, (
#                 ticket_id,
#                 "Assigned",
#                 assigned_to,
#                 now
#             ))

#         if resolution_note:
#             cursor.execute("""
#                 INSERT INTO ticket_updates (
#                     ticket_id,
#                     update_type,
#                     details,
#                     updated_at
#                 )
#                 VALUES (?, ?, ?, ?)
#             """, (
#                 ticket_id,
#                 "Resolution Note",
#                 resolution_note,
#                 now
#             ))

#         connection.commit()
#         connection.close()

#         logger.info(
#             f"Ticket updated successfully: {ticket_id}"
#         )

#         return True

#     def delete_ticket(self, ticket_id):
#         connection = get_connection()
#         cursor = connection.cursor()

#         cursor.execute(
#             "DELETE FROM tickets WHERE ticket_id = ?",
#             (ticket_id,)
#         )

#         connection.commit()
#         connection.close()

#         logger.info(
#             f"Ticket deleted successfully: {ticket_id}"
#         )

#         return True

#     def get_ticket_updates(self, ticket_id):
#         connection = get_connection()
#         cursor = connection.cursor()

#         cursor.execute("""
#             SELECT *
#             FROM ticket_updates
#             WHERE ticket_id = ?
#             ORDER BY id DESC
#         """, (ticket_id,))

#         updates = cursor.fetchall()

#         connection.close()

#         return updates








from datetime import datetime
import sqlite3

from database.database import get_connection
from utils.logger import logger


class TicketService:

    def generate_ticket_id(self):
        connection = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "SELECT ticket_id FROM tickets ORDER BY rowid DESC LIMIT 1"
            )

            result = cursor.fetchone()

            if result:
                number = int(result[0][1:]) + 1
            else:
                number = 1

            return f"T{number:03d}"

        except (sqlite3.Error, ValueError) as error:
            logger.exception("Error generating ticket ID")
            raise RuntimeError(
                f"Unable to generate ticket ID: {error}"
            )

        finally:
            if connection:
                connection.close()

    def create_ticket(self, ticket):
        connection = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ticket.ticket_id = self.generate_ticket_id()
            ticket.created_at = now
            ticket.updated_at = now

            cursor.execute("""
                INSERT INTO tickets (
                    ticket_id,
                    requester_name,
                    email,
                    title,
                    category,
                    priority,
                    description,
                    status,
                    assigned_to,
                    created_at,
                    updated_at,
                    resolved_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                ticket.ticket_id,
                ticket.requester_name,
                ticket.email,
                ticket.title,
                ticket.category,
                ticket.priority,
                ticket.description,
                ticket.status,
                ticket.assigned_to,
                ticket.created_at,
                ticket.updated_at,
                ticket.resolved_at
            ))

            connection.commit()

            logger.info(
                f"Ticket created successfully: {ticket.ticket_id}"
            )

            return ticket

        except sqlite3.IntegrityError as error:
            if connection:
                connection.rollback()

            logger.exception(
                f"Ticket creation failed: {error}"
            )

            raise ValueError(
                f"Unable to create ticket: {error}"
            )

        except sqlite3.Error as error:
            if connection:
                connection.rollback()

            logger.exception(
                f"Database error while creating ticket: {error}"
            )

            raise RuntimeError(
                "A database error occurred while creating the ticket."
            )

        finally:
            if connection:
                connection.close()

    def get_all_tickets(self):
        connection = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "SELECT * FROM tickets ORDER BY rowid DESC"
            )

            return cursor.fetchall()

        except sqlite3.Error as error:
            logger.exception(
                f"Error retrieving tickets: {error}"
            )

            raise RuntimeError(
                "Unable to retrieve tickets."
            )

        finally:
            if connection:
                connection.close()

    def get_ticket(self, ticket_id):
        connection = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "SELECT * FROM tickets WHERE ticket_id = ?",
                (ticket_id,)
            )

            return cursor.fetchone()

        except sqlite3.Error as error:
            logger.exception(
                f"Error retrieving ticket {ticket_id}: {error}"
            )

            raise RuntimeError(
                "Unable to retrieve the ticket."
            )

        finally:
            if connection:
                connection.close()

    def search_tickets(self, keyword):
        connection = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            keyword = f"%{keyword}%"

            cursor.execute("""
                SELECT * FROM tickets
                WHERE ticket_id LIKE ?
                   OR requester_name LIKE ?
                   OR title LIKE ?
            """, (
                keyword,
                keyword,
                keyword
            ))

            return cursor.fetchall()

        except sqlite3.Error as error:
            logger.exception(
                f"Error searching tickets: {error}"
            )

            raise RuntimeError(
                "Unable to search tickets."
            )

        finally:
            if connection:
                connection.close()

    def update_ticket(
        self,
        ticket_id,
        status=None,
        priority=None,
        assigned_to=None,
        resolution_note=None
    ):
        connection = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute("""
                UPDATE tickets
                SET status = COALESCE(?, status),
                    priority = COALESCE(?, priority),
                    assigned_to = COALESCE(?, assigned_to),
                    updated_at = ?
                WHERE ticket_id = ?
            """, (
                status,
                priority,
                assigned_to,
                now,
                ticket_id
            ))

            if cursor.rowcount == 0:
                logger.warning(
                    f"Ticket not found for update: {ticket_id}"
                )
                return False

            if status:
                cursor.execute("""
                    INSERT INTO ticket_updates (
                        ticket_id,
                        update_type,
                        details,
                        updated_at
                    )
                    VALUES (?, ?, ?, ?)
                """, (
                    ticket_id,
                    "Status Changed",
                    status,
                    now
                ))

            if priority:
                cursor.execute("""
                    INSERT INTO ticket_updates (
                        ticket_id,
                        update_type,
                        details,
                        updated_at
                    )
                    VALUES (?, ?, ?, ?)
                """, (
                    ticket_id,
                    "Priority Changed",
                    priority,
                    now
                ))

            if assigned_to:
                cursor.execute("""
                    INSERT INTO ticket_updates (
                        ticket_id,
                        update_type,
                        details,
                        updated_at
                    )
                    VALUES (?, ?, ?, ?)
                """, (
                    ticket_id,
                    "Assigned",
                    assigned_to,
                    now
                ))

            if resolution_note:
                cursor.execute("""
                    INSERT INTO ticket_updates (
                        ticket_id,
                        update_type,
                        details,
                        updated_at
                    )
                    VALUES (?, ?, ?, ?)
                """, (
                    ticket_id,
                    "Resolution Note",
                    resolution_note,
                    now
                ))

            connection.commit()

            logger.info(
                f"Ticket updated successfully: {ticket_id}"
            )

            return True

        except sqlite3.Error as error:
            if connection:
                connection.rollback()

            logger.exception(
                f"Error updating ticket {ticket_id}: {error}"
            )

            raise RuntimeError(
                "Unable to update the ticket."
            )

        finally:
            if connection:
                connection.close()

    def delete_ticket(self, ticket_id):
        connection = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "DELETE FROM tickets WHERE ticket_id = ?",
                (ticket_id,)
            )

            if cursor.rowcount == 0:
                logger.warning(
                    f"Ticket not found for deletion: {ticket_id}"
                )
                return False

            connection.commit()

            logger.info(
                f"Ticket deleted successfully: {ticket_id}"
            )

            return True

        except sqlite3.Error as error:
            if connection:
                connection.rollback()

            logger.exception(
                f"Error deleting ticket {ticket_id}: {error}"
            )

            raise RuntimeError(
                "Unable to delete the ticket."
            )

        finally:
            if connection:
                connection.close()

    def get_ticket_updates(self, ticket_id):
        connection = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("""
                SELECT *
                FROM ticket_updates
                WHERE ticket_id = ?
                ORDER BY id DESC
            """, (ticket_id,))

            return cursor.fetchall()

        except sqlite3.Error as error:
            logger.exception(
                f"Error retrieving ticket history {ticket_id}: {error}"
            )

            raise RuntimeError(
                "Unable to retrieve ticket history."
            )

        finally:
            if connection:
                connection.close()