from rest_framework import serializers

from .models import BackGroundField


class BackGroundFieldCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackGroundField
        fields = ["id", "producer", "whole_sale", "service", "created_at", "updated_at"]


class BackGroundFieldDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackGroundField
        fields = ["id", "producer", "whole_sale", "service", "created_at", "updated_at"]
        depth = 1
