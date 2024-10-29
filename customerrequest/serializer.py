from customerrequest.models import CustomerRequests, FacilityMaster, FacilityHasAppLink
from rest_framework import serializers



class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequests
        fields = "__all__"
        validators = [
            # UniqueValidator
            # UniqueTogetherValidator
        ]



class FacilityHasAppLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityHasAppLink
        fields = "__all__"



class FacilityMasterSerializer(serializers.ModelSerializer):
    facility_has_app_link = FacilityHasAppLinkSerializer(read_only=True)

    class Meta:
        model = FacilityMaster
        fields = "__all__"


class CreateFacilityHasAppLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityHasAppLink
        fields = ["play_store_link",
                  "app_store_link",
                  "deep_link",
                  "short_play_store_link",
                  "short_app_store_link",
                  "short_deep_link"]