from django.db import models

from customerrequest.models import CustomerRequestTypeDefn
from customerrequest.models.mastermodels import FacilityMaster


# Create your models here.
class FacilityHasRequestType(models.Model):
    facility_req_type_code = models.CharField(max_length = 100)
    facility_req_type_name = models.CharField(max_length = 200)
    facility_id = models.ForeignKey(FacilityMaster, on_delete = models.CASCADE)
    cust_req_type_id = models.ForeignKey(CustomerRequestTypeDefn, on_delete = models.CASCADE)
    crt_date = models.TimeField(auto_now = True)
    crt_rsn = models.CharField(max_length = 100)
    crt_by = models.CharField(max_length = 100)
    upd_date = models.TimeField(auto_now = True, null=True, blank=True)
    upd_rsn = models.CharField(max_length = 100, null=True, blank=True)
    upd_by = models.CharField(max_length = 100, null=True, blank=True)


