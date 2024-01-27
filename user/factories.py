from django.contrib.auth import get_user_model
import factory
from factory.django import DjangoModelFactory

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.sequence(lambda n: "user_{}".format(n))
    first_name = "John"
    last_name = "Doe"
    email = factory.sequence(lambda n: "test{}@example.com".format(n))
    password = "password"


