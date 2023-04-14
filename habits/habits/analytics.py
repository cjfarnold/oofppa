import habits.models as models
from django.db.models import Max, Min
from datetime import datetime, timedelta, date
import pandas as pd

class Analytics():
    def __init__(self) -> None:
        pass

    def longrunnstreak(self):
        maxsd = models.analytics.objects.aggregate(Max('streakduration'))['streakduration__max']
        return list(models.analytics.objects.filter(streakduration=maxsd).values('name','streakduration'))
     
    def longrunstreakforhabit(self, hid):

        maxsd = models.analytics.objects.filter(habitid_id=hid).aggregate(Max('streakduration'))['streakduration__max']
        return list(models.analytics.objects.filter(streakduration=maxsd).values('name','streakduration'))

    def  sameperiodicity(self):
        rs = models.tracker.objects.order_by('habitid_id','htype').select_related('habitid_id').values('habitid_id__name','startdate','enddate','htype').distinct()
    
        return list(rs)
    
    def struggling(self):

        maxsd = models.analytics.objects.aggregate(Min('streakduration'))['streakduration__min']
        return list(models.analytics.objects.filter(streakduration=maxsd).values('name','streakduration'))
    

# Adding place holder