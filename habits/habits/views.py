from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from habits.habit import habits

def getHabits(request):

    if request.method == 'GET':
        hb = habits
        return HttpResponse(hb.list_habits()) 

@csrf_exempt
def addHabits(request):

    if request.method == "POST":
        data = request.body
        body = json.loads(data)
        name = body['name']
        htype = body['htype']
        duration = body['duration']
        hb = habits(name,htype,duration)
        result = hb.add_habit()
        print(result)
        return HttpResponse(result['result'], content_type="application/json")
        #return HttpResponse("done", content_type="application/json")