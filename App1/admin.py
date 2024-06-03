from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()
from . models import *

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass

admin.site.register(driver)
admin.site.register(passenger)

