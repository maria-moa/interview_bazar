from django.contrib import admin
from .models import Service

# Register your models here.


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    pass
