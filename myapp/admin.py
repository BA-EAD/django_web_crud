from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.db import models

# Register your models here.

class Hello(UserAdmin):
	model = User
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login', 'is_superuser')

class UserBrowser(models.Model):
    browser_name = models.CharField(max_length=50)


admin.site.unregister(User)
admin.site.register(User, Hello)
admin.site.register(Registr)