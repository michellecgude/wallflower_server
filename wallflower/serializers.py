
from rest_framework import serializers

from .models import Mood, Habit, Meditation, UpliftingContent

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