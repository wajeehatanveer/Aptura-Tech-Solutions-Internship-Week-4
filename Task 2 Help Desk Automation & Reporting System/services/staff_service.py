import sqlite3

from database.database import get_connection
from utils.logger import logger


class StaffService:

    def add_staff(self, staff):
        connection = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO staff (
                    staff_id,
                    name,
                    email,
                    department,
                    role,
                    availability
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                staff.staff_id,
                staff.name,
                staff.email,
                staff.department,
                staff.role,
                staff.availability
            ))

            connection.commit()

            logger.info(
                f"Staff member added successfully: {staff.staff_id}"
            )

            return True

        except sqlite3.IntegrityError as error:
            if connection:
                connection.rollback()

            logger.exception(
                f"Staff creation failed: {error}"
            )

            raise ValueError(
                f"Unable to add staff member: {error}"
            )

        except sqlite3.Error as error:
            if connection:
                connection.rollback()

            logger.exception(
                f"Database error while adding staff: {error}"
            )

            raise RuntimeError(
                "A database error occurred while adding staff."
            )

        finally:
            if connection:
                connection.close()

    def get_all_staff(self):
        connection = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("""
                SELECT *
                FROM staff
                ORDER BY name
            """)

            return cursor.fetchall()

        except sqlite3.Error as error:
            logger.exception(
                f"Error retrieving staff: {error}"
            )

            raise RuntimeError(
                "Unable to retrieve staff records."
            )

        finally:
            if connection:
                connection.close()

    def get_staff(self, staff_id):
        connection = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "SELECT * FROM staff WHERE staff_id = ?",
                (staff_id,)
            )

            return cursor.fetchone()

        except sqlite3.Error as error:
            logger.exception(
                f"Error retrieving staff {staff_id}: {error}"
            )

            raise RuntimeError(
                "Unable to retrieve staff member."
            )

        finally:
            if connection:
                connection.close()

    def update_staff(
        self,
        staff_id,
        name=None,
        email=None,
        department=None,
        role=None,
        availability=None
    ):
        connection = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("""
                UPDATE staff
                SET name = COALESCE(?, name),
                    email = COALESCE(?, email),
                    department = COALESCE(?, department),
                    role = COALESCE(?, role),
                    availability = COALESCE(?, availability)
                WHERE staff_id = ?
            """, (
                name,
                email,
                department,
                role,
                availability,
                staff_id
            ))

            if cursor.rowcount == 0:
                logger.warning(
                    f"Staff member not found for update: {staff_id}"
                )
                return False

            connection.commit()

            logger.info(
                f"Staff member updated successfully: {staff_id}"
            )

            return True

        except sqlite3.Error as error:
            if connection:
                connection.rollback()

            logger.exception(
                f"Error updating staff {staff_id}: {error}"
            )

            raise RuntimeError(
                "Unable to update staff member."
            )

        finally:
            if connection:
                connection.close()

    def delete_staff(self, staff_id):
        connection = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "DELETE FROM staff WHERE staff_id = ?",
                (staff_id,)
            )

            if cursor.rowcount == 0:
                logger.warning(
                    f"Staff member not found for deletion: {staff_id}"
                )
                return False

            connection.commit()

            logger.info(
                f"Staff member deleted successfully: {staff_id}"
            )

            return True

        except sqlite3.Error as error:
            if connection:
                connection.rollback()

            logger.exception(
                f"Error deleting staff {staff_id}: {error}"
            )

            raise RuntimeError(
                "Unable to delete staff member."
            )

        finally:
            if connection:
                connection.close()

    def get_available_staff(self):
        connection = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("""
                SELECT *
                FROM staff
                WHERE availability = 'Available'
                ORDER BY name
            """)

            return cursor.fetchall()

        except sqlite3.Error as error:
            logger.exception(
                f"Error retrieving available staff: {error}"
            )

            raise RuntimeError(
                "Unable to retrieve available staff."
            )

        finally:
            if connection:
                connection.close()