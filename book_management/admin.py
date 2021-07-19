from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import book

@register(book)
class bookAdmin(admin.ModelAdmin):
    list = ['name','ISBN_number']


