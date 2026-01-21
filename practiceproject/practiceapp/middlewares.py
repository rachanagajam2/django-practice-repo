import json
from django.http import JsonResponse

# it is global middleware it accepting all api requestes
class middleware1:
    def __init__(self,get_response):
        self.get_response=get_response
        print("middleware1 is intiationg")
    def __call__(self,request):
        if request.path== "/first/":
            print("middlewarre1 is accectping requests")
        response=self.get_response(request)
        return response
# for specific request
class middleware2:
    def __init__(self,get_response):
        self.get_response=get_response
        print("middleware2 is intiationg")
    def __call__(self,request):
        if request.path== "/second/":
            print("middlewarre2 is accectping requests")
        response=self.get_response(request)
        return response

# example multiple middlewares for single example
# validation for reqirement to apply jobs
# scc and madicallly fit and  age
class sscMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        if request.path=='/job1/':
         incoming_data= json.loads(request.body)
         ssc_status=incoming_data.get("ssc_status")
         if ssc_status:
          response=self.get_response(request) #it gives eesponse from views
          return response
         return  JsonResponse({"status":"failure","msg":"u should qualify the ssc to apply for this job"})


class medicallyFitMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
     if request.path=='/job1/':
        incoming_data= json.loads(request.body)
        medical_status=incoming_data.get("medical_status")
        if medical_status:
         response=self.get_response(request) #it gives eesponse from views
         return response
        return  JsonResponse({"status":"failure","msg":"u should qualify the medaically to apply for this job"})
       

class ageValidationMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
     if request.path=='/job1/':
        incoming_data= json.loads(request.body)
        age=incoming_data.get("age")
        if age>21:
         response=self.get_response(request) #it gives eesponse from views
         return response
        return  JsonResponse({"status":"failure","msg":"u should have ateast 21 to apply for this job"})
       