from django.db import models

from customerrequest.models import FacilityHasRequestType, FacilityMaster, UnitMaster, PersonMaster


class CustomerRequests(models.Model):
    cust_req_code = models.CharField(max_length = 50)
    # facility_req_type_id = models.ForeignKey(FacilityHasRequestType, on_delete=models.CASCADE)
    # facility_id = models.ForeignKey(FacilityMaster, on_delete=models.CASCADE)
    # unit_id = models.ForeignKey(UnitMaster, on_delete=models.CASCADE)
    # person_id = models.ForeignKey(PersonMaster, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now = False, auto_now_add=True)
    completion_date = models.DateTimeField(null = True, blank=True)
    request_json = models.TextField(max_length = 4294967295)
    crt_date = models.DateTimeField(auto_now=True)
    crt_rsn = models.CharField(max_length=100)
    crt_by = models.CharField(max_length=100)
    upd_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    upd_rsn = models.CharField(max_length=100, null=True, blank=True)
    upd_by = models.CharField(max_length=100, null=True, blank=True)