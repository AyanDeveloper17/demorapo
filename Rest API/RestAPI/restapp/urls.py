from django.urls import path
from restapp import views

urlpatterns = [
    path('',views.apiview,name='apiview'),
    path('task-list/',views.tasklist,name='tasklist'),
    path('task-details/<str:pk>/',views.taskdetails,name='taskdetails'),
    path('task-create/',views.taskcreate,name='taskcreate'),
    path('task-update/<str:pk>',views.taskupdate,name='taskupdate'),
    path('task-delete/<str:pk>',views.taskdelete,name='taskdelete'),
    
]
