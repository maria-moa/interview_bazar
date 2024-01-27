from rest_framework import generics
from .serializers import ServiceSerializer

from .models import Service
from bases.permissions import IsAdminOrReadonlyPermission


class ServiceListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadonlyPermission]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadonlyPermission]
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    lookup_field = "id"
    lookup_url_kwarg = "service_id"
