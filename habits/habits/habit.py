'''
This is the habits class file this is used to add a new habit to the application and create tracker enteries
in the tracker model

'''

import habits.models as models
from datetime import datetime, timedelta, date
import habits.tracker as tracker

class habits():
    def __init__(self, name, htype, duration) -> None:
        self.name = name
        self.htype = htype
        self.duration = duration

# This function is use to add habit into the habits table and call the tracker class add to tracker method which makes 
# entries into the tracker table whic will be used to track the progress made to the habits     
    def add_habit(self):
        # dic = {
        #     "name":self.name,
        #     "htype":self.htype,
        #     "duration":self.duration
        # }
        # return dic
        #print("******************")
        #print(""+self.name+"::::"+self.htype+"::::"+str(self.duration))
        #habit = models.habits.objects.create(self.name,self.htype,self.duration)
        h = models.habits(name=self.name,htype=self.htype,duration=self.duration)
        h.save()
        habitid = models.habits.objects.get(name=self.name).id  

        tr = tracker.Tracker(htype=self.htype,task_state=False,due_date="2000-01-01",updated_date= "2000-01-01",start_date="2000-01-1",end_date="2000-01-1",habit_state= False)
        result = tr.add_totracker(habitid,str(date.today()),self.duration)
        #print(result)
        if result["status"] == "added":
             res = {"result":self.name}
             return res
        else:
             res = {"result":"Error"}
             return res
        #return "done"

    # def updateHabit():
    #     pass

# The list_habits() function is use to list the habits when the user wants to update the status of a particular habit
#     
    def list_habits():
    
        hnames = models.habits.objects.values("name","id")

        return hnames
    # Adding place holder