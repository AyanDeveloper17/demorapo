from django.urls import path
from aggregateapp import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('tb/<slug:table_slug>/',views.table,name='table'),
    path('tb/<int:id>/',views.table,name='table'),
    # path('mv/',views.my_view,name='my_view'),

    
]