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
#path params if we are expecting single record is available
def getstudentbycourse(request,course_param):
    try:
        if request.method=="GET":
            data=CourseRegistration.objects.get(course=course_param) #get will give only one boject it doesn't work on multiple onjects related to one
            print(data)
            responseObject={"name":data.name,"email":data.email,"course":data.course,"phone":data.phone}
            return JsonResponse({"status":"success","msg":"records fected","data":responseObject})
        
        return JsonResponse({"msg":"only get"})
    except:
        return JsonResponse({"status":"error","msg":"somethimng went wrong"})
#multiple records based on filteration (sir didn't explain total explanation)
def getmultiplestudents(request,course):
    try:
         if request.method=="GET":
             data=(CourseRegistration.objects.filter(course=course))
             final=list(data.values("name","email","course","phone"))
             if len(final)==0:
                 msg="no records found"
             else:
                 msg="records fetched successfully"
             return JsonResponse({"status":"success","no.of records":len(final),"msg":msg,"data":final})
         return JsonResponse({"msg":"only get"})
    except Exception as e:
        return JsonResponse({"status":"error","msg":"somethimng went wrong"})
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
            return JsonResponse({"Status":"error","meaasge":e})
    return JsonResponse({"message":"Please try on POST method only"})

student_info = [
    {"id": 1, "name": "vasanth", "degree": "EEE"},
    {"id": 2, "name": "krishna", "degree": "ECE"},
    {"id": 3, "name": "kiran", "degree": "CSF"},
    {"id": 4, "name": "Anvesh", "degree": "EEE"},
]

# Path parameter example in normal server
def getStudentById(request, id):
    filteredStudent = []

    for student in student_info:
        if id == student["id"]:
            filteredStudent.append(student)

    return JsonResponse({"data": filteredStudent})


# Query parameter example using @csrf_exempt in postman 
@csrf_exempt
def getStudentsByDegree(request,deg):
 try:
    if request.method=="GET":
       degreeBasedFilteration = []
   
       for student in student_info:
           if deg==student["degree"]:
               degreeBasedFilteration.append(student)
       if len(degreeBasedFilteration)==0:
           msg="no records found"
       else:
           msg="students record fetched successfully"
       return JsonResponse({"status":"success","no.of records":len(degreeBasedFilteration),"data": degreeBasedFilteration,"msg":msg})
    return JsonResponse({"status":"failure","msg":"only get is allowed"})
 except Exception as e :
     return JsonResponse({"status":"error","msg":"somthing went wrong"})
