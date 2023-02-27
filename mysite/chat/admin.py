from django.contrib import admin

# Register your models here.
from .models import userlogin,Messages

# Register your models here.
admin.site.register(userlogin)
admin.site.register(Messages)