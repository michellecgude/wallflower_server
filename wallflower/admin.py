from django.contrib import admin
from .models import User, Profile, Mood, Meditation, UpliftingContent

admin.site.register([User, Profile, Mood, Meditation, UpliftingContent])