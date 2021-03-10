from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Mood, Habit, Meditation, UpliftingContent
from .serializers import MoodSerializer, HabitSerializer, MeditationSerializer, UpliftingContentSerializer

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