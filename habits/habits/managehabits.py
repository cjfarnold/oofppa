import requests
import questionary
import json

topmenue = questionary.select("Wellcome to Habit Tracker: \n What would you like to do?",
                   choices=["List all existing habits","Add a new Habit","Update a Habit","Analyze your Habits"]).ask()
if topmenue == "List all existing habits":
    response = requests.get("http://127.0.0.1:8000/listhabits/")
    obj = json.loads(response.text)
    for i in range(len(obj)):
        #print(i)
        print(str(obj[i]["id"])+":"+obj[i]["name"]+"\n")
if topmenue == "Add a new Habit":
    name = questionary.text("Enter Name of the Habit").ask()
    type = questionary.select("Select Type",choices=['weekly','daily']).ask()
    duration = questionary.text("Enter Duration").ask()
    body = {"name":name,"htype":type,"duration":int(duration)}
    response = requests.post("http://127.0.0.1:8000/addhabits/", json=body)
    if response.status_code == 200:
        print("Habit added")
    else:
        print("check values entered")
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
            print("Status Updated for:"+str(date)+" as "+status)
        else:
            print("Error in updating the record")
    else:
        ("Status Updated for:"+str(date)+"as "+status)    

endmenue = questionary.select("Wellcome to Habit Tracker: \n What would you like to do?",
                   choices=["List all existing habits","Add a new Habit","Update a Habit","Analyze your Habits","Exit App"]).ask()
