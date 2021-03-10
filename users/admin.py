from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AbstractUserCreationForm, AbstractUserChangeForm
from .models import User

class AbstractUserAdmin(admin.ModelAdmin):
    add_form = AbstractUserCreationForm
    form = AbstractUserChangeForm
    model = User
    list_display = ['first_name', 'last_name', 'username', 'email', 'role']


admin.site.register(User, AbstractUserAdmin)
