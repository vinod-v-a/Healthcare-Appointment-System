from django.db import models
from django.conf import settings


class Doctor(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_profile"
    )

    specialization = models.CharField(max_length=255)

    experience_years = models.PositiveIntegerField()

    hospital_name = models.CharField(max_length=255)

    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.specialization}"