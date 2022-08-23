from django.contrib import admin
from .models import *

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_name','id','age']
admin.site.register(Author,AuthorAdmin)

admin.site.register(Publisher)

class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name','id','book_price','get_author_name','book_page','publisher','pub_date']
admin.site.register(Book,BookAdmin)