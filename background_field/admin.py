from django.contrib import admin

from background_field.models import  BackGroundField



@admin.register(BackGroundField)
class BackGroundFieldAdmin(admin.ModelAdmin):
    pass
