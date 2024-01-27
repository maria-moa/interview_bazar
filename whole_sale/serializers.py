from rest_framework import serializers

from .models import WholeSale


class WholeSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WholeSale
        fields = ["id", "name", "created_at", "updated_at"]
