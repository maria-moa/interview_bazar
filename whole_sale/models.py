from django.db import models

from bases.model import BaseModel


class WholeSale(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name
