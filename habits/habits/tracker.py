import habits.models as models
from datetime import datetime, timedelta

class Tracker():
    
    def __init__(self, htype, task_state, due_date, updated_date, start_date, end_date, habit_state) -> None:
        
        self.htype = htype
        self.task_state = task_state
        self.due_date = due_date
        self.updated_date = updated_date
        self.start_date = start_date
        self.end_date = end_date
        self.habit_state = habit_state
    
    def add_totracker(self,habitid,startdate,duration):
    #    print(self.htype,habitid,startdate,str(duration))
        if self.htype == "daily":
            print("inside daily if")
            habittype = "daily"
            for i  in range(0,duration):
    #            print("inside if "+str(i))
                if i == 0:
                    due = startdate
                else:
                    due = str(datetime.strptime(startdate,'%Y-%m-%d').date() + timedelta(days=i))
                end = str(datetime.strptime(startdate,'%Y-%m-%d').date() + timedelta(days=duration))
                t = models.tracker(habitid=models.habits.objects.get(id=habitid),
                                          htype=habittype,
                                          taskstate=self.task_state,
                                          duedate=due,
                                          updateddate=self.updated_date,
                                          startdate=str(datetime.strptime(startdate,'%Y-%m-%d').date()),
                                          enddate=end,
                                          habitsstate=self.habit_state)
                t.save()
            res = {"status":"added"}
            return res
       
        elif self.htype == "weekly":
            habittype = "weekly"
            for i  in range(0,duration):
                if i == 0:
                    due = self.due_date
                else:
                    due = str(datetime.strptime(self.due_date,'%Y-%m-%d').date() + timedelta(days=i+7))
                end = str(datetime.strptime(self.due_date,'%Y-%m-%d').date() + timedelta(days=duration*7))
                t = models.tracker(habitid=models.habits.objects.get(id=habitid),
                                          htype=habittype,
                                          taskstate=self.task_state,
                                          duedate=due,
                                          updateddate=self.updated_date,
                                          startdate=str(datetime.strptime(startdate,'%Y-%m-%d').date()),
                                          enddate=end,
                                          habitsstate=self.habit_state)
                t.save()
            res = {"status":"added"}
            return res
        


    def update_task(self):
        pass
    def compute_streak(self):
        pass
    def schedule_compute_streak(self):
        pass
''' 
                "habitid":1,
            "htype":"daily",
            "taskstate":"True",
            "duedate":"2023-02-21",
            "updateddate":"2023-02-21",
            "startdate":"2023-02-17",
            "enddate":"2023-03-17",
            "habitsstate":"False"
'''