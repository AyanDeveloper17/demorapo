from django.urls import path
from .views import *

urlpatterns = [
    path('',calculate,name='calculate'),
]
