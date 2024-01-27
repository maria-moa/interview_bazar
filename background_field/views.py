from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import BackGroundField
from .permissions import BackGroundFieldRetrieveDestroyPermission
from .serializers import BackGroundFieldCreateSerializer, BackGroundFieldDetailSerializer


class BackGroundFieldCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BackGroundFieldCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class RetrieveMyBackGroundFieldView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BackGroundFieldDetailSerializer
    queryset = BackGroundField.objects.all()

    def get_object(self):
        return (
            BackGroundField.objects
            .filter(user=self.request.user)
            .prefetch_related("producer", "whole_sale", "service")
            .first()
        )


class BackGroundFieldRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, BackGroundFieldRetrieveDestroyPermission]

    queryset = BackGroundField.objects.all()

    def get_serializer_class(self):
        if self.request.method.upper() == "GET":
            return BackGroundFieldDetailSerializer
        return BackGroundFieldCreateSerializer

    lookup_field = "id"
    lookup_url_kwarg = "background_field_id"
