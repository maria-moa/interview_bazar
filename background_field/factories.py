import factory
from factory.django import DjangoModelFactory

from user.factories import UserFactory
from .models import BackGroundField


class BackGroundFieldFactory(DjangoModelFactory):
    class Meta:
        model = BackGroundField

    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def producers(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.producers.add(*extracted)

    @factory.post_generation
    def whole_sales(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.whole_sales.add(*extracted)

    @factory.post_generation
    def services(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.services.add(*extracted)




