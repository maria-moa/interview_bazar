from django.db import models
from bases.model import BaseModel


class Service(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name

