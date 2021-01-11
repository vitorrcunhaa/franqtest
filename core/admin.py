from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.forms import CustomUserChangeForm, SignUpForm
from core.models import User


class CustomUserAdmin(BaseUserAdmin):
    model = User
    add_form = SignUpForm
    form = CustomUserChangeForm
    list_display = ('username', 'email', 'phone', 'balance')


admin.site.register(User, CustomUserAdmin)
