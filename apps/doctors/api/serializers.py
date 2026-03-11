from rest_framework import serializers
from apps.doctors.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = [
            "id",
            "user",
            "specialization",
            "experience_years",
            "hospital_name",
            "consultation_fee",
            "is_available",
            "created_at",
        ]

        read_only_fields = ["id", "created_at"]