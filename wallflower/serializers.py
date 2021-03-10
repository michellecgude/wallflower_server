
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from .models import Mood, Habit, Meditation, UpliftingContent

class MoodSerializer(serializers.ModelSerializer):
    permission_classes = (IsAuthenticated,)
    class Meta:
        model = Mood
        fields = ("id", "user", "mood_type", "created_at", "note_entry") 

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ("id", "user", "name", "description", "created_at", "note_entry")

class MeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meditation
        fields = ("id", "user", "name", "benefit", "length", "type_of_meditation", "meditation_link")

class UpliftingContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpliftingContent
        fields = ("id", "user", "description", "img_url", "src", "article_link")