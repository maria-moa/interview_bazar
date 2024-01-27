import factory
from factory.django import DjangoModelFactory
from .models import WholeSale


class WholeSaleFactory(DjangoModelFactory):
    class Meta:
        model = WholeSale

    name = factory.sequence(lambda n: "wholesale_{}".format(n))



