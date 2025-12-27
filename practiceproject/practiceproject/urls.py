"""
URL configuration for practiceproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from registrations.views import inserting_data,get_students
from registrations.views import getStudentById, getStudentsByDegree,getstudentbycourse,getmultiplestudents,BookMyshow,getmoviesbyscreen,getmulmoviesbyscreen,insert_movies,moviesbygenre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',inserting_data),
    path('get_reg/',get_students),
    path("student/<int:id>/", getStudentById),
    path("students/<str:deg>/", getStudentsByDegree),
    path("getcourse/<str:course_param>/",getstudentbycourse),
    path("getmulcourse/<str:course>/",getmultiplestudents),
    path("bookshow/",BookMyshow),
    path("moviebyscreen/<str:screen>/",getmoviesbyscreen),
    path("moviebyscreens/<str:first>/<str:second>/",getmulmoviesbyscreen),
    path("insert_movies/",insert_movies),
    path("moviesbygenre/<str:genre>/",moviesbygenre)
]
