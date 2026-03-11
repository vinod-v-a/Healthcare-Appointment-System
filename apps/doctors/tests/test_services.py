import pytest
from apps.doctors.services.doctor_service import create_doctor_profile
from apps.users.tests.factories import UserFactory
from apps.doctors.models import Doctor

pytestmark = pytest.mark.django_db


def test_create_doctor_profile_success():

    user = UserFactory(role="DOCTOR")

    doctor = create_doctor_profile({
        "user": user,
        "specialization": "Cardiology",
        "experience_years": 10,
        "hospital_name": "Apollo",
        "consultation_fee": 500
    })

    assert doctor.id is not None
    assert doctor.user == user
    assert doctor.specialization == "Cardiology"


def test_create_doctor_profile_invalid_role():

    user = UserFactory(role="PATIENT")

    with pytest.raises(ValueError):

        create_doctor_profile({
            "user": user,
            "specialization": "Cardiology",
            "experience_years": 10,
            "hospital_name": "Apollo",
            "consultation_fee": 500
        })


def test_doctor_saved_in_database():

    user = UserFactory(role="DOCTOR")

    create_doctor_profile({
        "user": user,
        "specialization": "Neurology",
        "experience_years": 8,
        "hospital_name": "AIIMS",
        "consultation_fee": 700
    })

    assert Doctor.objects.count() == 1