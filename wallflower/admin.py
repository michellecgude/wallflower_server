from django.contrib import admin
from .models import User, UserProfile, Mood, Habit, Meditation, UpliftingContent 

# Register your models here.
admin.site.register([User, UserProfile, Mood, Habit, Meditation, UpliftingContent])