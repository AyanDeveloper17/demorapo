from django.urls import path
from .views import *

urlpatterns = [
    path('',login,name='login'),
    path('reg/',register,name='register'),
    # path('auth/',authenticate,name='authenticate'),
    # path('ft/',faltu,name='faltu'),
]
