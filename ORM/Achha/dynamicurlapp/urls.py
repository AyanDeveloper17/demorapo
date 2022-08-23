from django.urls import path
from dynamicurlapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dynamic/<ayan_id>',views.dynamic,name='dynamic'),
    path('converter/<int:pk>',views.converter,name='converter'),
    path('doubleid/<int:a_id>/<y_id>',views.doubleid,name='doubleid'),
    
]