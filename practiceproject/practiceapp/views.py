import json
import jwt
from practiceapp.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password,check_password
from datetime import datetime,timedelta
from django.conf import settings
from django.utils import timezone


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

@csrf_exempt
def signup(request):
     if request.method != "POST":
        return JsonResponse({"error": "use POST method"})
     try:
        data = json.loads(request.body)
        hashed_password=make_password(data["password"])
     
        user=User.objects.create(
          username=data["username"],
          email=data["email"],
          password=hashed_password,
          role=data["role"]
       )
        return JsonResponse({"status":"success","msg":"user registered successfully"})
     except KeyError:
           return JsonResponse({
            "error": "Missing required fields"
        }, status=400)
     except Exception as e:
        return JsonResponse({"error": str(e)})

@csrf_exempt
def login(request):
     user_info=json.loads(request.body)
     username=user_info.get("username")
     user_existing_info=list(User.objects.filter(username=username).values())
     payload={"username":username,
              "role":user_existing_info[0].get("role"),
              "iat":datetime.utcnow(),
              "exp":datetime.utcnow()+timedelta(seconds=settings.JWT_EXP_TIME)
              }
     token=jwt.encode(payload,settings.JWT_SECRET_KEY,algorithm=settings.JWT_ALGORITHM)
     return JsonResponse({
          "status":"success","msg":"login successful","greetings":f"welcome {username}","token":token
     })
@csrf_exempt
def protected_api(request):
    if request.method != "POST":
        return JsonResponse({"msg": "Only POST method allowed"}, status=405)

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return JsonResponse(
            {"msg": "Authorization header missing"},
            status=401
        )

    try:
        # Expecting: "Bearer <token>"
        parts = auth_header.split()

        if len(parts) != 2 or parts[0] != "Bearer":
            return JsonResponse(
                {"msg": "Invalid Authorization header format"},
                status=401
            )

        token = parts[1]
        print(token)  # reading token from input

        decoded_payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )

        print(decoded_payload)

        if decoded_payload.get("role") == "admin":
            return JsonResponse({"msg": "You have access for this API"})
        else:
            return JsonResponse(
                {"msg": "You do not have access for this API"},
                status=403
            )

    except jwt.ExpiredSignatureError:
        return JsonResponse({"msg": "Token has expired"}, status=401)

    except jwt.InvalidTokenError:
        return JsonResponse({"msg": "Invalid token"}, status=401)

    except Exception as e:
        return JsonResponse(
            {"msg": "Something went wrong", "error": str(e)},
            status=500
        )
