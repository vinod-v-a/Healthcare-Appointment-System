import pytest
from apps.doctors.api.serializers import DoctorSerializer
from apps.doctors.tests.factories import DoctorFactory
from apps.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db

def test_doctor_serializer_valid_data():
    user = UserFactory()

    data = {
        "user": user.id,
        "specialization": "Cardiology",
        "experience_years": 10,
        "hospital_name": "Apollo Hospital",
        "consultation_fee": 500
    }

    serializer = DoctorSerializer(data=data)

    assert serializer.is_valid()
    
def test_doctor_serializer_invalid_data():
    user = UserFactory()

    data = {
        "user": user.id,
        "specialization": "Cardiology",
        "experience_years": "ten",
        "hospital_name": "Apollo Hospital",
        "consultation_fee": 500
    }

    serializer = DoctorSerializer(data=data)

    assert not serializer.is_valid()
    

def test_doctor_serializer_missing_fields():
    data = {}

    serializer = DoctorSerializer(data=data)

    assert not serializer.is_valid()

def test_doctor_serializer_output():
    doctor = DoctorFactory()

    serializer = DoctorSerializer(instance=doctor)

    data = serializer.data

    assert data["id"] == doctor.id
    assert data["specialization"] == doctor.specialization

