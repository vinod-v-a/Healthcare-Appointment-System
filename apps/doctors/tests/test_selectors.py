import pytest
from apps.doctors.selectors.doctor_selector import (
    get_doctor_by_id,
    get_all_doctors,
    get_available_doctors,
)
from apps.doctors.tests.factories import DoctorFactory

pytestmark = pytest.mark.django_db

def test_get_doctor_by_id():
    doctor = DoctorFactory()

    result = get_doctor_by_id(doctor.id)

    assert result == doctor
    
def test_get_all_doctors():
    DoctorFactory()
    DoctorFactory()
    DoctorFactory()

    doctors = get_all_doctors()

    assert doctors.count() == 3


def test_get_available_doctors():
    DoctorFactory(is_available=True)
    DoctorFactory(is_available=True)
    DoctorFactory(is_available=False)

    doctors = get_available_doctors()

    assert doctors.count() == 2
    

