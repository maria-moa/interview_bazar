from django.contrib.auth import get_user_model
from django.db import models, IntegrityError

from bases.internal_exceptions import DuplicatedBackGroundFieldPerUser
from bases.model import BaseModel
from product.models import Product
from service.models import Service
from whole_sale.models import WholeSale

User = get_user_model()


class BackGroundField(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    producer = models.ManyToManyField(Product)
    whole_sale = models.ManyToManyField(WholeSale)
    service = models.ManyToManyField(Service)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.pk)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        try:
            return super().save(
                force_insert=force_insert,
                force_update=force_update,
                using=using,
                update_fields=update_fields,
            )
        except IntegrityError as e:
            # Add an one of possible way to monitor this event
            if self.__class__.objects.filter(user_id=self.user_id).exists():
                raise DuplicatedBackGroundFieldPerUser
            raise e
