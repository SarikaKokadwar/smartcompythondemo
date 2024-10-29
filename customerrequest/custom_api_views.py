from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CustomerRequests
from .serializer import CustomerRequestSerializer


class CustomerRequestListCreateAPIView(APIView):
    def get(self, request):
        # filter options : __eq, __gt, __gte, __lt, __lte, __in, __range
        # allrequests = CustomerRequests.objects.all().filter(id__range=[1,4])

        # Write raw sql stmt... stored procedure wont be able to call
        # allrequests = CustomerRequests.objects.raw("select * from customerrequest_customerrequests")

        allrequests = CustomerRequests.objects.all()
        serialized = CustomerRequestSerializer(allrequests, many=True)
        return Response(serialized.data)


    def post(self, request):
        serialized = CustomerRequestSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=400)

        serialized.save()
        return Response(serialized.data, status=201)

