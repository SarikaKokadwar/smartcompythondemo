from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# from facilitylinks.models import FacilityHasAppLink
# from facilitylinks.serializer import FacilityHasAppLinkSerializer


# Create your views here.
# class FacilityHasAppLinkListCreateAPIView(ListCreateAPIView):
#     query_set = FacilityHasAppLink.objects.all()
#     serializer_class = FacilityHasAppLinkSerializer
#
#
# class FacilityHasAppLinkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     query_set = FacilityHasAppLink.objects.all()
#     serializer_class = FacilityHasAppLinkSerializer
#     lookup_field = 'id'