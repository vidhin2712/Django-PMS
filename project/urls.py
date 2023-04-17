from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/',ProjectIndexView.as_view(),name='index'),
    path('desk/',Desk.as_view(),name='desk'),
    path('mail',confirmMail,name='confirm_mail'),

    path('dashboard',Dashboard.as_view(),name='dashboard'),
    path('project-detail/<int:pk>/',ProjectDetail.as_view(),name='projectdetail'),
    path('project-update/<int:pk>/',ProjectUpdate.as_view(),name='projectupdate'),
    path('project-delete/<int:pk>/',ProjectDelete.as_view(),name='projectdelete'),

    path('task',ProjectTask.as_view(),name='task'),

    path('team-register/',TeamRegister.as_view(),name='teamregister'),
    path('team-detail/<int:pk>/',TeamDetail.as_view(),name='teamdetail'),
    path('team-delete/<int:pk>/',TeamDelete.as_view(),name='teamdelete'),
    
    path('logout/',LogoutView.as_view(),name='logout'),

    path('module-create',ProjectModuleCreate.as_view(),name='projectmodule'),
    path('module-detail/<int:pk>',ProjectModuleDetail.as_view(),name='projectmoduledetail'),
    path('module-update/<int:pk>',ProjectModuleUpdate.as_view(),name='projectmoduleupdate'),
    path('module-delete/<int:pk>',ProjectModuleDelete.as_view(),name='projectmoduledelete'),

    path('task-create',TaskCreate.as_view(),name='taskcreate'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='taskupdate'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='taskdelete'),

    path('user-task-create/',UserTaskView.as_view(),name='taskdelete'),
    
]
