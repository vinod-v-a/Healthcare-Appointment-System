from django.urls import path
from apps.doctors.api.views import (
    DoctorCreateView,
    DoctorListView,
    DoctorDetailView
)

urlpatterns = [

    path("create/", DoctorCreateView.as_view(), name="doctor-create"),

    path("", DoctorListView.as_view(), name="doctor-list"),

    path("<int:doctor_id>/", DoctorDetailView.as_view(), name="doctor-detail"),
]