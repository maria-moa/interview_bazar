import factory
from factory.django import DjangoModelFactory
from .models import Product


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.sequence(lambda n: "product_{}".format(n))



