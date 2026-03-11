import factory
from apps.doctors.models import Doctor
from apps.users.tests.factories import UserFactory


class DoctorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Doctor

    user = factory.SubFactory(UserFactory)

    specialization = factory.Faker("job")
    experience_years = factory.Faker("random_int", min=1, max=20)
    hospital_name = factory.Faker("company")
    consultation_fee = factory.Faker("random_int", min=200, max=1000)
    is_available = True