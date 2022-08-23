from django.contrib import admin
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','id','teacher_id','teacher','last_name','mobile','email')
admin.site.register(Student,StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_data = ('teacher_name','id')
admin.site.register(Teacher,TeacherAdmin)
