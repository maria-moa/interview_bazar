from rest_framework import generics
from .serializers import WholeSaleSerializer

from .models import WholeSale
from bases.permissions import IsAdminOrReadonlyPermission


class WholeSaleListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadonlyPermission]
    queryset = WholeSale.objects.all()
    serializer_class = WholeSaleSerializer


class WholeSaleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadonlyPermission]
    serializer_class = WholeSaleSerializer
    queryset = WholeSale.objects.all()

    lookup_field = "id"
    lookup_url_kwarg = "wholeSale_id"
