from django.db import models

# Create your models here.
class CustomerRequestTypeDefn(models.Model):
    cust_req_type_code = models.CharField(max_length =100)
    cust_req_type_name = models.CharField(max_length=200)
    column_description = models.TextField(max_length = 4294967295)
    crt_date = models.TimeField(auto_now = True)
    crt_rsn = models.CharField(max_length = 100)
    crt_by = models.CharField(max_length = 100)
    upd_date = models.TimeField(auto_now = True, null=True, blank=True)
    upd_rsn = models.CharField(max_length = 100, null=True, blank=True)
    upd_by = models.CharField(max_length = 100, null=True, blank=True)


class CustomerRequestHasStatusType(models.Model):
    cust_req_status_type_code = models.CharField(max_length = 100)
    cust_req_status_type_name = models.CharField(max_length = 200)
    crt_date = models.TimeField(auto_now = True)
    crt_rsn = models.CharField(max_length = 100)
    crt_by = models.CharField(max_length = 100)
    upd_date = models.TimeField(auto_now = True, null=True, blank=True)
    upd_rsn = models.CharField(max_length = 100, null=True, blank=True)
    upd_by = models.CharField(max_length = 100, null=True, blank=True)


class FacilityTypeDefn(models.Model):
    facility_type_code = models.CharField(max_length = 20)
    facility_type_name = models.CharField(max_length=100)
    facility_type_desc = models.CharField(max_length=500)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null = True, blank=True)
    crt_date = models.DateTimeField(auto_now=True)
    crt_rsn = models.CharField(max_length=100)
    crt_by = models.CharField(max_length=100)
    upd_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    upd_rsn = models.CharField(max_length=100, null=True, blank=True)
    upd_by = models.CharField(max_length=100, null=True, blank=True)
