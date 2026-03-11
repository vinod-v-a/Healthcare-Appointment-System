import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from apps.users.tests.factories import UserFactory
from apps.doctors.tests.factories import DoctorFactory


pytestmark = pytest.mark.django_db


class TestDoctorAPI:

    def setup_method(self):
        self.client = APIClient()

    def test_create_doctor_authenticated(self):
        """
        Verify that a doctor profile can be created
        when the user is authenticated and has DOCTOR role.
        """

        user = UserFactory(role="DOCTOR")

        self.client.force_authenticate(user=user)

        url = reverse("doctor-create")

        data = {
            "specialization": "Cardiology",
            "experience_years": 10,
            "hospital_name": "Apollo Hospital",
            "consultation_fee": 500
        }

        response = self.client.post(url, data, format="json")

        assert response.status_code in [200, 201]
        assert response.data["specialization"] == "Cardiology"

    def test_create_doctor_requires_authentication(self):
        """
        Verify that unauthenticated users cannot create doctor profiles.
        """

        url = reverse("doctor-create")

        data = {
            "specialization": "Cardiology",
            "experience_years": 10,
            "hospital_name": "Apollo Hospital",
            "consultation_fee": 500
        }

        response = self.client.post(url, data, format="json")

        assert response.status_code == 401

    def test_list_doctors(self):
        """
        Verify that the API returns all doctors.
        """

        DoctorFactory()
        DoctorFactory()
        DoctorFactory()

        url = reverse("doctor-list")

        response = self.client.get(url)

        assert response.status_code == 200
        assert len(response.data) == 3

    def test_get_doctor_detail(self):
        """
        Verify fetching a single doctor by ID.
        """

        doctor = DoctorFactory()

        url = reverse("doctor-detail", kwargs={"doctor_id": doctor.id})

        response = self.client.get(url)

        assert response.status_code == 200
        assert response.data["id"] == doctor.id

    def test_get_doctor_not_found(self):
        """
        Verify API returns 404 for non-existent doctor.
        """

        url = reverse("doctor-detail", kwargs={"doctor_id": doctor.id})

        response = self.client.get(url)

        assert response.status_code == 404