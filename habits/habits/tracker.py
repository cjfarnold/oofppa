import habits.models as models
from datetime import datetime, timedelta, date
import pandas as pd

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
                    due = str(datetime.strptime(due,'%Y-%m-%d').date() + timedelta(days=1))
                end = str(datetime.strptime(startdate,'%Y-%m-%d').date() + timedelta(days=duration-1))
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
                    due = startdate
                else:
#                    due = str(datetime.strptime(startdate,'%Y-%m-%d').date() + timedelta(days=i+7))
                    due = str(datetime.strptime(due,'%Y-%m-%d').date() + timedelta(weeks=1))
                end = str(datetime.strptime(startdate,'%Y-%m-%d').date() + timedelta(weeks=(duration-1)))
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
        


    def update_task(self, habitid, due_date, status ):
        u = models.tracker.objects.filter(habitid=habitid,duedate=due_date).update(taskstate=status)
        s = Tracker.compute_streak(self, habitid)
        if s == True:
            if u:
                return {"result":"success"}
            else:
                return {"result":"faild"}
        else:
            return {"result":"AnalyticsupdateFailed"}


    def compute_streak(self, hid):
        taskstate_list = models.tracker.objects.filter(habitid=hid[0]).values_list("taskstate", flat=True)
        l = [i for i in taskstate_list]
        print(l)
        df = pd.DataFrame({'taskstate':l})
        df['Streak'] = df['taskstate'].groupby((df['taskstate'] != df['taskstate'].shift()).cumsum()).cumcount() + 1
        df1 = df.groupby(['taskstate']).max()
        print(df1)
       # return df1.at[True,'Streak']
        streaklength = df1.at[True,'Streak']
        print("Streak Lenght :"+str(streaklength))
        if streaklength >=6:
            resultset = models.analytics.objects.filter(habitid=hid[0]).values("habitid","runinstance")
            print(resultset)
            if not resultset:
                #id = hid[0]
                instance = 1
                data = {"name":models.habits.objects.filter(id=hid[0]).values("name")[0]['name'],
                            "habittype":models.habits.objects.filter(id=hid[0]).values("htype")[0]['htype'],
                            "streak":True,
                            "streakduration":streaklength,
                            "runinstance":instance,
                            "updateddate":str(datetime.strptime(str(date.today()),'%Y-%m-%d').date())
                        }
                 
                 
                res = models.analytics.filter(habitid=models.habits.objects.get(id=hid[0]),
                                                                        name=data["name"],
                                                                        habittype=models.habits.objects.filter(id=hid[0]).values("htype")[0]['htype'],
                                                                        streak=data["streak"],
                                                                        streakduration=data["streakduration"],
                                                                        runinstance=data["runinstance"],
                                                                        updateddate=data["updateddate"]
                                                                        )
                res.save()
                return True
            else:
                resultset = models.analytics.objects.filter(habitid=hid[0]).values("habitid","runinstance","streakduration").last()
                instance = resultset['runinstance']
                instance +=1
                streakduration = resultset['streakduration']
                print("instance "+str(instance)+" Tableduration :"+str(streakduration))
                data = {"name":models.habits.objects.filter(id=hid[0]).values("name")[0]['name'],
                            "habittype":models.habits.objects.filter(id=hid[0]).values("htype")[0]['htype'],
                            "streak":True,
                            "streakduration":streaklength,
                            "runinstance":instance,
                            "updateddate":str(datetime.strptime(str(date.today()),'%Y-%m-%d').date())
                        }
                 
                if streakduration < streaklength:
                    print("Streak duration <"+str(streaklength))
                    res = models.analytics.objects.filter(habitid=models.habits.objects.get(id=hid[0])).update(runinstance=instance,streakduration=streaklength)
                    #res.save()
                    return True
                return "same duration as earlier streak"
        
# Adding place holder