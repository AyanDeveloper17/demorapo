from django.urls import path
from restapp2 import views
urlpatterns = [
    # path('',views.create,name='create'),
    # path('show/',views.show,name='show'),
    # path('del/<int:id>',views.delete,name='delete'),
    # # path('update/<int:pk>',views.update,name='update'),
    # path('upd/<int:pk>',views.update_student,name='update'),
    path('studentapi/',views.StudentApi.as_view(),name='studentapi')
    ]
