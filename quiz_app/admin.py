from django.contrib import admin
from quiz_app.models import (
    Subject,
    Question,
    # Option
)

# Register your models here.
# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ['subject_name']

admin.site.register(Subject)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['subject','question_name']

admin.site.register(Question,QuestionAdmin)

# class OptionAdmin(admin.ModelAdmin):
#     list_display = ['question','op1','op2','op3','op4','answer']

# admin.site.register(Option,OptionAdmin)
