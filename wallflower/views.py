from rest_framework import viewsets
from rest_framework import permissions

from .models import User, UserProfile, Mood, Habit, Meditation, UpliftingContent
from .serializers import UserSerializer, UserProfileSerializer, MoodSerializer, HabitSerializer, MeditationSerializer, UpliftingContentSerializer

class UserProfileView(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = (permissions.AllowAny,)


class MoodView(viewsets.ModelViewSet):
    serializer_class = MoodSerializer
    queryset = Mood.objects.all()
    permission_classes = (permissions.AllowAny,)


class HabitView(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (permissions.AllowAny,)


class MeditationView(viewsets.ModelViewSet):
    serializer_class = MeditationSerializer
    queryset = Meditation.objects.all()
    permission_classes = (permissions.AllowAny,)


class UpliftingContentView(viewsets.ModelViewSet):
    serializer_class = UpliftingContentSerializer
    queryset = UpliftingContent.objects.all()
    permission_classes = (permissions.AllowAny,)



