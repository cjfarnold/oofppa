import habits.models as models
from datetime import datetime, timedelta, date
import pandas as pd

class Analytics():
    def __init__(self) -> None:
        pass

    def longrunnstreak(self, hid):
        lrs = models.analytics.objects.filter('streakduration').values('name','streakduration')
        return lrs.aggregate(max('streakduration'))
    
    def  sameperiodicity(self):
        rs = models.tracker.objects.order_by('habitid_id','htype').values('habitid_id','startdate','enddate','htype').distinct()
        #sp = rs.values('habitid_id').order_by('habitid_id')
        return list(rs)
