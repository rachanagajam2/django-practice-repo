from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def first(request):
    return render(request,'first.html')
def second(request):
    return render(request, 'second.html')

@csrf_exempt
def job1(request):
    try:
        if request.method=="POST":
            return  JsonResponse({"status":"success","mesage":"job1 applied successfully"})
        return JsonResponse({"status":"failure","message0":"only post method is valid"})
    except Exception as e:
                return JsonResponse({"status":"error","message":"something went wrong"})
