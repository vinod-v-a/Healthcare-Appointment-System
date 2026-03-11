from django.contrib.auth import get_user_model
from apps.doctors.models import Doctor

User = get_user_model()


def create_doctor_profile(data):

    user = data.get("user")

    if not user:
        raise ValueError("User must be provided")

    # Validate user role
    if user.role != "DOCTOR":
        raise ValueError("Only users with DOCTOR role can create a doctor profile")

    doctor = Doctor.objects.create(
        user=user,
        specialization=data.get("specialization"),
        experience_years=data.get("experience_years"),
        hospital_name=data.get("hospital_name"),
        consultation_fee=data.get("consultation_fee"),
    )

    return doctor