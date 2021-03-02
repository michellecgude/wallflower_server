from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AbstractUserCreationForm, AbstractUserChangeForm
from .models import User, UserProfile

class AbstractUserAdmin(UserAdmin):
    add_form = AbstractUserCreationForm
    form = AbstractUserChangeForm
    model = User
    list_display = ['email', 'username']

admin.site.register(User, AbstractUserAdmin)
admin.site.register(UserProfile)
