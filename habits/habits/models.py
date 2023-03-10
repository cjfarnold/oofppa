from django.db import models

class habits(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    htype = models.CharField(max_length=50)
    duration = models.IntegerField()


class tracker(models.Model):
    id = models.IntegerField(primary_key=True)
    habitid = models.ForeignKey(habits, on_delete=models.CASCADE)
    htype = models.CharField(max_length=50)
    taskstate = models.BooleanField()
    duedate = models.DateField()
    updateddate = models.DateField()
    startdate = models.DateField()
    enddate = models.DateField()
    habitsstate = models.BooleanField()

class analytics(models.Model):
    id = models.IntegerField(primary_key=True)
    habitid = models.ForeignKey(habits, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    habittype = models.CharField(max_length=50)
    streak = models.BooleanField()
    streakduration = models.IntegerField()
    runinstance = models.IntegerField()
    updateddate = models.DateField()
    