from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from customerrequest.models import FacilityMaster, FacilityHasAppLink
from customerrequest.serializer import FacilityMasterSerializer, FacilityHasAppLinkSerializer, \
    CreateFacilityHasAppLinkSerializer


class FacilityListCreateAPIView(APIView):
    # queryset = FacilityMaster.objects.all()
    # serializer_class = FacilityMasterSerializer

    def get(self, request):
        # select_related is when current table is referring to other table (one to one)
        # prefetch_selected is when current table is referred in other table (one to many)
        facilities = FacilityMaster.objects.all().select_related("facilityhasapplink")
        return Response(FacilityMasterSerializer(facilities, many=True).data)


    def post(self, request):
        serialized = FacilityMasterSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=401)

        serialized.save()
        return Response(serialized.data, status=201)



class FacilityListRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FacilityMaster.objects.all()
    serializer_class = FacilityMasterSerializer


class FacilityHasAppLinkListCreateAPIView(APIView):
    serializer_class = FacilityHasAppLinkSerializer

    def post(self,request, facility_id):
        facility = get_object_or_404(FacilityMaster, pk=facility_id)
        serialized = CreateFacilityHasAppLinkSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=400)

        facility_app_links = FacilityHasAppLink(
            play_store_link = serialized.validated_data["play_store_link"],
            app_store_link=serialized.validated_data["app_store_link"],
            deep_link=serialized.validated_data["deep_link"],
            short_play_store_link=serialized.validated_data["short_play_store_link"],
            short_app_store_link=serialized.validated_data["short_app_store_link"],
            short_deep_link=serialized.validated_data["short_deep_link"],
            facility = facility
        )
        facility_app_links.save()

        facility.facility_has_app_link = facility_app_links
        facility.save()

        return Response(FacilityHasAppLinkSerializer(facility_app_links).data, status=201)


class FacilityHasAppLinkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    query_set = FacilityHasAppLink.objects.all()
    serializer_class = FacilityHasAppLinkSerializer
    lookup_field = 'id'