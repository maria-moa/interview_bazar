from rest_framework import generics
from .serializers import ProductSerializer

from .models import Product
from bases.permissions import IsAdminOrReadonlyPermission


class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadonlyPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAdminOrReadonlyPermission]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    lookup_field = "id"
    lookup_url_kwarg = "product_id"

