from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from habits.habit import habits
from habits.tracker import Tracker
from habits.analytics import Analytics

def getHabits(request):

    if request.method == 'GET':
        hb = habits
        return JsonResponse(list(hb.list_habits()),safe=False)

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

@csrf_exempt
def updateHabit(request):
    if request.method == "POST":
        requdata = request.body
        data = json.loads(requdata)
        habitid = data['habitid'],
        due_date = data['due_date']
        status = data['status']
        tr = Tracker(htype="",task_state=False,due_date="2000-01-01",updated_date= "2000-01-01",start_date="2000-01-1",end_date="2000-01-1",habit_state= False)
        result = tr.update_task(habitid=habitid,due_date=due_date,status=status)

        return HttpResponse(result["result"],content_type="application/json")
@csrf_exempt
def streak(request, habitid):
    if request.method == "GET":
        tr = Tracker(htype="",task_state=False,due_date="2000-01-01",updated_date= "2000-01-01",start_date="2000-01-1",end_date="2000-01-1",habit_state= False)
        count = tr.compute_streak(habitid=habitid)
        return HttpResponse(count, content_type="application/json")
    
@csrf_exempt
def streak_test(request, habitid):
    if request.method == "GET":
        tr = Tracker(htype="",task_state=False,due_date="2000-01-01",updated_date= "2000-01-01",start_date="2000-01-1",end_date="2000-01-1",habit_state= False)
        result = tr.compute_streak(habitid)
        return HttpResponse(result, content_type="application/json")
    
@csrf_exempt
def sameperiodicity(request):
    
    if request.method == 'GET':
        a = Analytics()
        rs = a.sameperiodicity()
        return JsonResponse(rs, safe=False)

@csrf_exempt
def longrunnstreak(request):
    if request.method == 'GET':
        a = Analytics()
        rs = a.longrunnstreak()
        return JsonResponse(rs, safe=False)

@csrf_exempt
def longrunstreakforhabit(request, habitid):
    if request.method == "GET":
        a = Analytics()
        rs = a.longrunstreakforhabit(habitid)
        return JsonResponse(rs, safe=False)

@csrf_exempt
def struggling(request):
    if request.method == 'GET':
        a = Analytics()
        rs = a.struggling()
        return JsonResponse(rs, safe=False)