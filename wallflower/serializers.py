
from rest_framework import serializers

from djoser.serializers import UserCreateSerializer, UserSerializer

from . import models

from .models import User, UserProfile, Mood, Habit, Meditation, UpliftingContent

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'username', 'password')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "user", "first_name", "last_name", "date_created", "role")

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ("id", "user", "name", "created_at", "note_entry", "role") 

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ("id", "user", "name", "description", "created_at", "note_entry")

class MeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meditation
        fields = ("id", "user", "name", "purpose", "benefit", "length", "type_of_meditation")

class UpliftingContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpliftingContent
        fields = ("id", "user", "description", "img_url", "src", "article_link")