from rest_framework import serializers

from djoser.serializers import UserCreateSerializer, UserSerializer

from . import models

from .models import User, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'email', 'username', 'password')

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "user", "first_name", "last_name", "date_created", "role")