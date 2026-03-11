from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.doctors.api.serializers import DoctorSerializer
from apps.doctors.services.doctor_service import create_doctor_profile
from apps.doctors.selectors.doctor_selector import (
    get_all_doctors,
    get_doctor_by_id
)


class DoctorCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        # Copy request data so we can inject the user
        data = request.data.copy()
        data["user"] = request.user.id

        serializer = DoctorSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        doctor = create_doctor_profile(serializer.validated_data)

        response_serializer = DoctorSerializer(doctor)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class DoctorListView(APIView):

    def get(self, request):

        doctors = get_all_doctors()

        serializer = DoctorSerializer(doctors, many=True)

        return Response(serializer.data)


class DoctorDetailView(APIView):

    def get(self, request, doctor_id):

        doctor = get_doctor_by_id(doctor_id)

        if not doctor:
            return Response(
                {"error": "Doctor not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DoctorSerializer(doctor)

        return Response(serializer.data)