from practiceapp.models import User
import re
import json
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password,check_password


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
            #it gives eesponse from views
             return self.get_response(request)
            return  JsonResponse({"status":"failure","msg":"u should qualify the ssc to apply for this job"})
        return self.get_response(request) 

class medicallyFitMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
     if request.path=='/job1/':
        incoming_data= json.loads(request.body)
        medical_status=incoming_data.get("medical_status")
        if medical_status:
          return self.get_response(request) #it gives eesponse from views
         
        return  JsonResponse({"status":"failure","msg":"u should qualify the medaically to apply for this job"})
     return self.get_response(request)  

class ageValidationMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        

    def __call__(self,request):
     if request.path=='/job1/':
        incoming_data= json.loads(request.body)
        age=incoming_data.get("age")
        if age>21:
         return self.get_response(request) #it gives eesponse from views
         
        return  JsonResponse({"status":"failure","msg":"u should have ateast 21 to apply for this job"})
     return self.get_response(request)
#================================
class authMiddleware:
   def __init__(self,get_response):
      self.get_response=get_response
      self.username_pattern = re.compile(r'^[a-zA-Z0-9_]{5,15}$')
      self.password_pattern = re.compile(r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#]{8,}$')
      self.email_pattern = re.compile(r'^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$')
   def __call__(self, request):
        if request.path in ["/signup/","/login/"] and request.method=="POST":
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({"error":"invalid JSON data"})

            if request.path =="/signup/":
                username = data.get("username")
                email = data.get("email")
                password = data.get("password")
                role=data.get("role")

                if not all([username, email, password,role]):
                    return JsonResponse({"error":"all fields are required"})
                if not self.username_pattern.match(username):
                    return JsonResponse({"error":"Invalide username format"})
                if not self.email_pattern.match(email):
                    return JsonResponse({"error":"Invalide email format"})
                if not self.password_pattern.match(password):
                    return JsonResponse({"error":"weak password"})
                if User.objects.filter(username=username).exists():
                    return JsonResponse({"error":"username already exists"})
                if User.objects.filter(email=email).exists():
                    return JsonResponse({"error":"email already exists"})
                
                # If it gets here, signup data is valid! 

            elif request.path == "/login/":
                username = data.get("username")
                password = data.get("password")
                if not all([username, password]):
                    return JsonResponse({"error":"all fields are required"})
                try:
                    user = User.objects.get(username=username)

                except User.DoesNotExist:
                    return JsonResponse({"error":"invalid username"})
                # if user.password != password:
                if not check_password(password,user.password):
                    return JsonResponse({"error":"invalid password"})
                
                # If it gets here, login data is valid!

        # This line must be reached for ALL successful paths!
        response = self.get_response(request)
        return response