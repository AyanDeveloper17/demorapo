from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name','id','customer_email']
admin.site.register(Customer,CustomerAdmin)
