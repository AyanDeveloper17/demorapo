from django.urls import path
from sessionapp import views

urlpatterns = [
  path('set/',views.setsession),
  path('get/',views.getsession),
  path('del/',views.delsession),

]