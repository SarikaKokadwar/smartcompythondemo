from django.db import models
from django.db.models import DO_NOTHING

from customerrequest.models import FacilityTypeDefn
# from facilitylinks.models import FacilityHasAppLink

class FacilityMaster(models.Model):
    facility_code = models.CharField(max_length =20)
    facility_name = models.CharField(max_length=500)
    facility_type_id = models.ForeignKey(FacilityTypeDefn, on_delete = models.CASCADE)
    facility_has_app_link = models.ForeignKey("FacilityHasAppLink",
                                              on_delete=DO_NOTHING,
                                              null=True,
                                              related_query_name="app_links" )
    crt_date = models.DateTimeField(auto_now = True)
    crt_rsn = models.CharField(max_length = 100)
    crt_by = models.CharField(max_length = 100)
    upd_date = models.DateTimeField(auto_now = True, null=True, blank=True)
    upd_rsn = models.CharField(max_length = 100, null=True, blank=True)
    upd_by = models.CharField(max_length = 100, null=True, blank=True)


class UnitMaster(models.Model):
    unit_code = models.CharField(max_length=50)
    unit_name = models.CharField(max_length=200)
    #unit_type_id = models.ForeignKey(UnitTypeDefn, on_delete=models.CASCADE)
    facility_id = models.ForeignKey(FacilityMaster, on_delete=models.CASCADE)
    #parent_unit_id = models.ForeignKey(UnitMaster, on_delete=models.CASCADE)
    extension_no = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    crt_date = models.DateTimeField(auto_now=True)
    crt_rsn = models.CharField(max_length=100)
    crt_by = models.CharField(max_length=100)
    upd_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    upd_rsn = models.CharField(max_length=100, null=True, blank=True)
    upd_by = models.CharField(max_length=100, null=True, blank=True)


class PersonMaster(models.Model):
    person_code = models.CharField(max_length = 50)
    facility_id = models.ForeignKey(FacilityMaster, on_delete=models.CASCADE)
    salutation = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    age_category = models.CharField(max_length=20)
    birth_date = models.DateTimeField()
    resident_flag = models.CharField(max_length=1)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    crt_date = models.DateTimeField(auto_now=True)
    crt_rsn = models.CharField(max_length=100)
    crt_by = models.CharField(max_length=100)
    upd_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    upd_rsn = models.CharField(max_length=100, null=True, blank=True)
    upd_by = models.CharField(max_length=100, null=True, blank=True)


class FacilityHasAppLink(models.Model):
    # facility = models.ForeignKey(FacilityMaster,
    #                                 on_delete=models.CASCADE,
    #                                 related_name = "facility_links")
    facility = models.OneToOneField(FacilityMaster,
                                    on_delete=models.DO_NOTHING,
                                    primary_key=True)
    play_store_link = models.CharField(max_length = 500)
    app_store_link = models.CharField(max_length=500)
    deep_link = models.CharField(max_length=500)
    short_play_store_link = models.CharField(max_length=500)
    short_app_store_link = models.CharField(max_length=500)
    short_deep_link = models.CharField(max_length=500)

    def __str__(self):
        return self.facility

