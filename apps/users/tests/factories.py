import factory
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: f"user{n}@test.com")
    full_name = factory.Faker("name")
    role = "DOCTOR"

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        password = extracted if extracted else "testpassword"
        self.set_password(password)
        if create:
            self.save()