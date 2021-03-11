from rest_framework import serializers

from djoser.serializers import UserCreateSerializer, UserSerializer

from . import models

from .models import User

# USER SERIALIZER
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'role')

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'role')