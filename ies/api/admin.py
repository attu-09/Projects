from django.contrib import admin
from .models import *

class teachersAdmin(admin.ModelAdmin):
    list_display = ['id','email','pas']

admin.site.register(teachers,teachersAdmin)
