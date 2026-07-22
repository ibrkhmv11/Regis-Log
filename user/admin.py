# user/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# CustomUser modelini admin panelda ko'rinadigan qilish
admin.site.register(CustomUser, UserAdmin)
