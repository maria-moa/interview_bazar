from rest_framework.permissions import BasePermission
from .models import BackGroundField


class BackGroundFieldRetrieveDestroyPermission(BasePermission):
    def has_object_permission(self, request, view, obj: BackGroundField):
        return obj.user == request.user


