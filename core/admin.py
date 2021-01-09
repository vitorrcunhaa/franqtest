from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import User


class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'phone')
    model = User


admin.site.register(User, CustomUserAdmin)
