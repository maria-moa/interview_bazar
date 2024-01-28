import factory
from factory.django import DjangoModelFactory
from .models import Service


class ServiceFactory(DjangoModelFactory):
    class Meta:
        model = Service

    name = factory.sequence(lambda n: "service_{}".format(n))
