from django.db import models

from customerrequest.models import FacilityMaster


# Create your models here.
# class FacilityHasAppLink(models.Model):
#     facility_id = models.ForeignKey(FacilityMaster,
#                                     on_delete=models.CASCADE,
#                                     related_name = "facility_links")
#     play_store_link = models.CharField(max_length = 500)
#     app_store_link = models.CharField(max_length=500)
#     deep_link = models.CharField(max_length=500)
#     short_play_store_link = models.CharField(max_length=500)
#     short_app_store_link = models.CharField(max_length=500)
#     short_deep_link = models.CharField(max_length=500)