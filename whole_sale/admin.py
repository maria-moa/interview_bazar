from django.contrib import admin
from .models import WholeSale


@admin.register(WholeSale)
class WholeSaleAdmin(admin.ModelAdmin):
    pass
