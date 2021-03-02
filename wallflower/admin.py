from django.contrib import admin
from .models import Mood, Habit, Meditation, UpliftingContent

admin.site.register([Mood, Habit, Meditation, UpliftingContent])