from django.contrib import admin

from customerrequest.models import CustomerRequestTypeDefn, CustomerRequestHasStatusType, FacilityMaster, \
    FacilityHasRequestType, FacilityTypeDefn

# Register your models here.

admin.site.register(FacilityTypeDefn)
admin.site.register(CustomerRequestTypeDefn)
admin.site.register(CustomerRequestHasStatusType)
admin.site.register(FacilityMaster)
admin.site.register(FacilityHasRequestType)