import pytest

from database.database import initialize_database
from models.staff import Staff
from services.staff_service import StaffService


@pytest.fixture
def staff_service(tmp_path, monkeypatch):
    """
    Create an isolated temporary database for testing.
    """

    import database.database as database_module

    test_database = tmp_path / "test_helpdesk.db"

    monkeypatch.setattr(
        database_module,
        "DATABASE_PATH",
        test_database
    )

    initialize_database()

    return StaffService()


@pytest.fixture
def sample_staff():
    return Staff(
        staff_id="S001",
        name="Test Staff",
        email="staff@example.com",
        department="IT",
        role="Support Agent",
        availability="Available"
    )


def test_add_staff(staff_service, sample_staff):

    result = staff_service.add_staff(
        sample_staff
    )

    assert result is True

    staff = staff_service.get_staff("S001")

    assert staff is not None
    assert staff[1] == "Test Staff"
    assert staff[2] == "staff@example.com"


def test_get_all_staff(staff_service, sample_staff):

    staff_service.add_staff(sample_staff)

    staff_records = staff_service.get_all_staff()

    assert len(staff_records) == 1


def test_get_staff(staff_service, sample_staff):

    staff_service.add_staff(sample_staff)

    staff = staff_service.get_staff("S001")

    assert staff is not None
    assert staff[0] == "S001"
    assert staff[1] == "Test Staff"


def test_update_staff(staff_service, sample_staff):

    staff_service.add_staff(sample_staff)

    result = staff_service.update_staff(
        "S001",
        name="Updated Staff",
        department="Support",
        role="Senior Support Agent",
        availability="Busy"
    )

    assert result is True

    updated_staff = staff_service.get_staff("S001")

    assert updated_staff[1] == "Updated Staff"
    assert updated_staff[3] == "Support"
    assert updated_staff[4] == "Senior Support Agent"
    assert updated_staff[5] == "Busy"


def test_get_available_staff(staff_service, sample_staff):

    staff_service.add_staff(sample_staff)

    available_staff = staff_service.get_available_staff()

    assert len(available_staff) == 1
    assert available_staff[0][0] == "S001"


def test_delete_staff(staff_service, sample_staff):

    staff_service.add_staff(sample_staff)

    result = staff_service.delete_staff("S001")

    assert result is True

    staff = staff_service.get_staff("S001")

    assert staff is None


def test_update_nonexistent_staff(staff_service):

    result = staff_service.update_staff(
        "S999",
        name="Unknown Staff"
    )

    assert result is False


def test_delete_nonexistent_staff(staff_service):

    result = staff_service.delete_staff("S999")

    assert result is False


def test_duplicate_staff_id(staff_service, sample_staff):

    staff_service.add_staff(sample_staff)

    duplicate_staff = Staff(
        staff_id="S001",
        name="Another Staff",
        email="another@example.com",
        department="IT",
        role="Support Agent",
        availability="Available"
    )

    with pytest.raises(ValueError):
        staff_service.add_staff(duplicate_staff)