import requests
import questionary
import json

def driverfunction():

    topmenue = questionary.select("Wellcome to Habit Tracker: \n What would you like to do?",
                   choices=["List all existing habits","Add a new Habit","Update a Habit","Analyze your Habits", "Exit App"]).ask()
    if topmenue == "List all existing habits":
        response = requests.get("http://127.0.0.1:8000/listhabits/")
        obj = json.loads(response.text)
        for i in range(len(obj)):
            #print(i)
            print("List of Habits are : \n")
            print(str(obj[i]["id"])+":"+obj[i]["name"]+"\n")
    if topmenue == "Add a new Habit":
        name = questionary.text("Enter Name of the Habit").ask()
        type = questionary.select("Select Type",choices=['weekly','daily']).ask()
        duration = questionary.text("Enter Duration").ask()
        body = {"name":name,"htype":type,"duration":int(duration)}
        response = requests.post("http://127.0.0.1:8000/addhabits/", json=body)
        if response.status_code == 200:
            print("Status: \n"+name+" : Habit added")
        else:
            print("Status: \n Check values entered")
    if topmenue == "Update a Habit":
        response = requests.get("http://127.0.0.1:8000/listhabits/")
        obj = json.loads(response.text)
        habitslist = []
        for i in range(len(obj)):
            t = str(obj[i]['id'])+":"+obj[i]["name"]
            habitslist.append(t)
        hlist = questionary.select("Select Type",choices=habitslist).ask()
        date = questionary.text("Enter Date in yyyy-mm-dd format").ask()
        status = questionary.select("Select Type",choices=["Completed","Missed"]).ask()
        id = hlist.split(":")[0]
        if status == "Completed":
            ubody = {"habitid":id,"due_date":date,"status":True}
            uresponse = requests.post("http://127.0.0.1:8000/updatehabit/", json=ubody)
            if uresponse.status_code == 200:
                print("\n Status Updated for:"+str(date)+" as "+status)
            else:
                print("\n Error in updating the record")
        else:
            ("\n Status Updated for:"+str(date)+"as "+status)    
    analyzelist = [ "1.List all currently tracked habits",
                    "2.List of all habits with the same periodicity",
                    "3.List the longest run streak of all defined habits",
                    "4.List the longest run streak for a given habit",
                    "5.list of the habits where the user was struggling with"
                    ]
    if topmenue == "Analyze your Habits":
        analysemenue = questionary.select("Analyze any of the following", choices=analyzelist).ask()
        choice = int(analysemenue.split(".")[0])
        if choice == 1:
            response = requests.get("http://127.0.0.1:8000/listhabits/")
            obj = json.loads(response.text)
            print("List of Habits are : \n")
            for i in range(len(obj)):
            #print(i)
                
                print(str(obj[i]["id"])+":"+obj[i]["name"]+"\n")
        
        if choice == 2:
            response = requests.get("http://127.0.0.1:8000/sameperiodicity/")
            obj = json.loads(response.text)
            print("List of Habits with sampe periodicity : \n")
            print("Habit Name: Habit Type: Start Date: End Date\n")
            for i in range(len(obj)):
            #print(i)
                print(str(obj[i]["habitid_id__name"])+": "+obj[i]["htype"]+": "+obj[i]["startdate"]+": "+obj[i]["enddate"]+"\n")

        if choice == 3:
            response = requests.get("http://127.0.0.1:8000/longrunnstreak/")
            obj = json.loads(response.text)
            print("The longest running streak of all defined habits : \n")
            for i in range(len(obj)):
            #print(i)
                print(str(obj[i]["name"])+":"+str(obj[i]["streakduration"])+"\n")
        
        if choice == 4:
            url = "http://127.0.0.1:8000/longrunstreakforhabit/"
            response = requests.get("http://127.0.0.1:8000/listhabits/")
            obj = json.loads(response.text)
            listofhabits = []
            for i in range(len(obj)):
                t = str(obj[i]['id'])+":"+obj[i]["name"]
                listofhabits.append(t)
            lrsh = questionary.select("Select a Habit:", choices=listofhabits).ask()
        #    print(lrsh)
            res = requests.get(url+lrsh.split(":")[0])
            resobj = json.loads(res.text)
            if len(resobj) == 0:
                print(" No streak completed for this Habit")
            else:
                for i in range(len(resobj)):
                    if resobj[i]['name'] == lrsh.split(":")[1]:
                        print("\n Longest streak for :"+resobj[i]["name"]+"is :"+str(resobj[i]["streakduration"]))
        #    print(resobj[0]['name'],str(resobj[0]['streakduration']))
        if choice == 5:
            response = requests.get("http://127.0.0.1:8000/struggling/")
            obj = json.loads(response.text)
            print("list of habits where the user is struggling with : \n")
            print("Habit Name: Streak Duration\n")
            for i in range(len(obj)):
            #print(i)
                
                print(str(obj[i]["name"])+": "+str(obj[i]["streakduration"])+"\n")                
    
    if topmenue == "Exit App":
        exit
    else:
        driverfunction()

if __name__ == "__main__":
    driverfunction()
# Adding place holder