import habits.models as models
from datetime import datetime, timedelta, date

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
        
        if u:
            return {"result":"success"}
        else:
            return {"result":"faild"}

    def compute_streak(self, habitid):
        count = models.tracker.objects.filter(habitid=habitid).count()
        duedatelist= models.tracker.objects.filter(habitid=habitid).values_list("duedate")
        l = []
        result = []
        run = 0
        data = {"name":"","habittype":""}
        for x in duedatelist:
            l.append(str(datetime.strptime(str(x[0]),'%Y-%m-%d').date()))
        cnt = 0
        streaklist = []
        for i in l:
            
            if models.tracker.objects.filter(duedate=i).values("taskstate") == True:
                cnt =cnt + 1
                if cnt >= 6:
                    streak = True
                    streaklenght = cnt
                    #streaklist.append({"habitid":habitid,"streakcount":[].append(streakcount)})
                    #cnt = 0
                else:
                    streak = False
                    cnt = 0
                    run = run + 1
                    data = {"name":models.habits.objects.filter(habitid=habitid).values("name"),
                            "habittype":models.habits.objects.filter(habitid=habitid).values("htype"),
                            "streak":True,
                            "streakduration":streaklenght,
                            "runinstance":run,
                            "updateddate":str(datetime.strptime(date.today(),'%Y-%m-%d').date())
                            }
            else:
                if run >=1:
                    result.append(data)

        for data in result:
            if models.analytics.objects.filter(habitid=habitid,runinstance=data["runinstance"]).values("habitid"):
                res = models.analytics.objects.filter(habitid=habitid).update(habitid=models.habits.objects.get(habitid=habitid),
                                                                        name=data["name"],
                                                                        habittype=models.habits.objects.filter(habitid=habitid).values("htype"),
                                                                        streak=data["streak"],
                                                                        streakduration=data["streakduration"],
                                                                        runinstance=data["runinstance"],
                                                                        updateddate=data["updateddate"]
                                                                        )
                if res:
                    return True
                else:
                    return False
            else:
                res = models.analytics(habitid=models.habits.objects.get(habitid=habitid),
                                                                        name=data["name"],
                                                                        habittype=models.habits.objects.filter(habitid=habitid).values("htype"),
                                                                        streak=data["streak"],
                                                                        streakduration=data["streakduration"],
                                                                        runinstance=data["runinstance"],
                                                                        updateddate=data["updateddate"]
                                                                        )
                res.save()
                return True

        return streaklist
        #return l
        #     duedate= models.tracker.objects.filter(habitid=habitid).values()["duedate"]
        #     if
        #return len(duedate)
        
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