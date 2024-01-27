from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductTypeAdmin(admin.ModelAdmin):
    pass
