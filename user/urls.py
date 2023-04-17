from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("login/",UserLogin.as_view(),name="login"),
    path("signup/",SignUp.as_view(),name="signup"),
    path("manager_register/",ManagerRegisterView.as_view(),name="manager_register"),
    path("teamleader_register/",TeamLeadeRegisterView.as_view(),name="teamleader_register"),
    path("developer_register/",DeveloperRegisterView.as_view(),name="developer_register"),
    path("tester_register/",TesterRegisterView.as_view(),name="tester_register"),

    path('temp',temp , name='temp'),
]