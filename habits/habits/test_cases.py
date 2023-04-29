import pytest
import requests
from datetime import datetime, timedelta, date
import json
import habits.models as models
from django.test import TestCase

class TestHabits(TestCase):

    def test_Addhabits(self):
        body = {"name":"daily_t",
            "htype":"daily",
            "duration":10}
        res = requests.post("http://127.0.0.1:8000/addhabits/", json=body)
        assert res.status_code == 200
    
    def test_Updatehabits(self):
        response = requests.get("http://127.0.0.1:8000/listhabits/")
        result = json.loads(response.text)
        for o in result:
            if o["name"] == "daily_t":
                id = o["id"]
        tdate = str(date.today()) # datetime.strptime(due,'%Y-%m-%d').date() 
        ubody = {"habitid":id,"due_date":str(datetime.strptime(str(date.today()),'%Y-%m-%d').date()),"status":True}
        print(ubody)
        uresponse = requests.post("http://127.0.0.1:8000/updatehabit/", json=ubody)
        print(uresponse.text)
        for i in range(1,10):
             ubody = {"habitid":id,"due_date":str(datetime.strptime(str(date.today()),'%Y-%m-%d').date()+timedelta(days=i)),"status":True}
             uresponse = requests.post("http://127.0.0.1:8000/updatehabit/", json=ubody)
        assert uresponse.status_code == 200
    
    def test_checkstreak(self):
        response = requests.get("http://127.0.0.1:8000/listhabits/")
        result = json.loads(response.text)
        for o in result:
            if o["name"] == "daily_t":
                id = o["id"]
        res = requests.get("http://127.0.0.1:8000/longrunstreakforhabit/"+str(id))
        assert res.status_code ==200

    def test_cleanup(self):
        response = requests.get("http://127.0.0.1:8000/listhabits/")
        result = json.loads(response.text)
        for o in result:
            if o["name"] == "daily_t":
                id = o["id"]
        
        input = {"id":id}
        response = requests.post("http://127.0.0.1:8000/deletetestrecords/",json=input)
        assert response.status_code == 200

