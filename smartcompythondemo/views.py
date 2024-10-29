from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from smartcompythondemo.models import Product
from smartcompythondemo.serializer import ProductSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]