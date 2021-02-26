from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User, UserProfile, Mood, Habit, Meditation, UpliftingContent

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'last_login', 'date_joined', 'is_staff')
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'date_created', 'role')

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ('name', 'created_at', 'note_entry')

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('name', 'description', 'created_at', 'note_entry')

class MeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meditation
        fields = ('name', 'purpose', 'benefit', 'length', 'type_of_meditation')

class UpliftingContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpliftingContent
        fields = ('title', 'description', 'img_url', 'src', 'article_link')