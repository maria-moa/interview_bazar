from django.contrib.auth import get_user_model
from django.db import models

from bases.model import BaseModel

User = get_user_model()


class Product(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]