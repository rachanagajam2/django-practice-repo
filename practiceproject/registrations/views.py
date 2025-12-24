from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CourseRegistration

# Create your views here.
def get_students(request):
     if request.method=="GET":
         registrations=CourseRegistration.objects.values()
         return JsonResponse({
             "registrations":list(registrations)
         })
     return JsonResponse({
         "message":"onlu GET method is allowed"
     })
@csrf_exempt
def inserting_data(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            CourseRegistration.objects.create(
                name=data["name"],
                email=data["email"],
                course=data["course"],
                phone=data["phone"]
                )
            return JsonResponse({"status":"succes","message":"Registration successful"})
        except Exception as e:
            return JsonResponse({"Status":"error","meaasge":str(e)})
    return JsonResponse({"message":"Please try on POST method only"})