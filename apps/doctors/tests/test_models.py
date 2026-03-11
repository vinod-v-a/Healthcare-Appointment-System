import pytest
from apps.doctors.tests.factories import DoctorFactory

pytestmark = pytest.mark.django_db


def test_doctor_creation():
    doctor = DoctorFactory()

    assert doctor.id is not None
    assert doctor.user is not None
    assert doctor.specialization is not None


def test_doctor_has_user():
    doctor = DoctorFactory()

    assert doctor.user is not None
    assert doctor.user.id is not None


def test_doctor_default_availability():
    doctor = DoctorFactory()

    assert doctor.is_available is True


def test_doctor_string_representation():
    doctor = DoctorFactory()

    assert str(doctor) != ""