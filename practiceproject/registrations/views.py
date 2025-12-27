from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CourseRegistration,MovieBooking




# Create your views here.
@csrf_exempt
def BookMyshow(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)

            MovieBooking.objects.create(
                moviename=data["movie_name"],
                showtime=data["show_time"],
                screenname=data["screen_name"]
            )

            return JsonResponse({
                "status": "success",
                "msg": "records inserted successfully"
            })

        return JsonResponse({
            "status": "failure",
            "message": "only POST method allowed"
        })

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": "something went wrong"
        })
@csrf_exempt
#single param
def getmoviesbyscreen(request,screen):
    try:
        if request.method=="GET":
            data=MovieBooking.objects.filter(screenname=screen).values()
            final_data=list(data)
            return JsonResponse({"status":"success",screen:final_data},status=200)
        return JsonResponse({"status":"failure","msg":"only get method is allowed"})
    except Exception as e:
        return JsonResponse({"status":"error","msg":"something went wrong"})
#multiple path params
def getmulmoviesbyscreen(request,first,second):
    try:
        if request.method=="GET":
            data1=MovieBooking.objects.filter(screenname=first).values()
            data2=MovieBooking.objects.filter(screenname=second).values()
            first_data=list(data1)
            second_data=list(data2)
            if len(first_data)==0:
                first_msg="no records"
            else:
                first_msg="records fetched"
            if len(second_data)==0:
                second_msg="no records"
            else:
                second_msg="records fetched"
            first_data.append(first_msg)
            second_data.append(second_msg)
            return JsonResponse({"status":"success",first:first_data,second:second_data},status=200)
        return JsonResponse({"status":"failure","msg":"only get method is allowed"})
    except Exception as e:
        return JsonResponse({"status":"error","msg":"something went wrong"})

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


#query params examples

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
