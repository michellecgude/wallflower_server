from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.serializers import ModelSerializer
from .models import User, UserProfile, Mood, Habit, Meditation, UpliftingContent

class UserSerializer(ModelSerializer): # user serializer for logged in users
    class Meta:
        model = User
        fields = ('username', 'email', 'last_login', 'date_joined', 'is_staff')

class UserSerializerWithToken(serializers.ModelSerializer): # used for handling signups

    token = serializers.SerializerMethodField()  #defining token field since user class doesn't have an internal 'token' field
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None) # used so serializer recognizes/stores password
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password) # properly hashes password
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password') # custom token field added to meta internal class for user
        
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