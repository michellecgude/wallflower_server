from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import User, UserProfile, Mood, Habit, Meditation, UpliftingContent
from .serializers import UserSerializer, UserProfileSerializer, MoodSerializer, HabitSerializer, MeditationSerializer, UpliftingContentSerializer

class UserProfileView(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = (permissions.AllowAny,)
    
class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class MoodList(generics.ListCreateAPIView):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer
class MoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer

class HabitList(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
class HabitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class MeditationList(generics.ListCreateAPIView):
    queryset = Meditation.objects.all()
    serializer_class = MeditationSerializer
class MeditationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meditation.objects.all()
    serializer_class = MeditationSerializer

class UpliftingContentList(generics.ListCreateAPIView):
    queryset = UpliftingContent.objects.all()
    serializer_class = UpliftingContentSerializer
class UpliftingContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UpliftingContent.objects.all()
    serializer_class = UpliftingContentSerializer