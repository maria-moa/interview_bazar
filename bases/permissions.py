from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser


class ReadOnlyPermission(BasePermission):
    @classmethod
    def has_permission(cls, request, view):
        return request.method in SAFE_METHODS


class IsAdminOrReadonlyPermission(BasePermission):
    def has_permission(self, request, view):
        return ReadOnlyPermission.has_permission(request=request, view=view) or IsAdminUser().has_permission(
            request=request, view=view
        )
