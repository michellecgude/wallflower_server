from django.contrib import admin
from .models import User, UserProfile, Mood, Habit, Meditation, UpliftingContent

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AbstractUserChangeForm, AbstractUserCreationForm
class AbstractUserAdmin(UserAdmin):    
    add_form = AbstractUserCreationForm
    form = AbstractUserChangeForm
    model = User
    list_display = ['email']

admin.site.register(User, AbstractUserAdmin)

# Register your models here.
admin.site.register([UserProfile, Mood, Habit, Meditation, UpliftingContent])