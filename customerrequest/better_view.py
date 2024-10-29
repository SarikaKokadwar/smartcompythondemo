from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import CustomerRequests
from .serializer import CustomerRequestSerializer


class CustomerRequestListCreateAPIView(ListCreateAPIView):
    queryset = CustomerRequests.objects.all()
    serializer_class = CustomerRequestSerializer


class CustomerRequestRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CustomerRequests.objects.all()
    serializer_class = CustomerRequestSerializer
    lookup_field = 'id'
