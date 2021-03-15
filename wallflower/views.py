from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    Mood, 
    FrontlineMeditation, 
    UnemployedMeditation, 
    SurvivorMeditation, 
    LossMeditation, 
    MentalHealthMeditation, 
    IsolatedMeditation, 
    FrontlineUpliftingContent, 
    UnemployedUpliftingContent, 
    SurvivorUpliftingContent, 
    LossUpliftingContent, 
    MentalHealthUpliftingContent, 
    IsolatedUpliftingContent)

from .serializers import (
    MoodSerializer, 
    FrontlineMeditationSerializer, 
    UnemployedMeditationSerializer, 
    SurvivorMeditationSerializer, 
    LossMeditationSerializer, 
    MentalHealthMeditationSerializer, 
    IsolatedMeditationSerializer, 
    FrontlineUpliftingContentSerializer, 
    UnemployedUpliftingContentSerializer, 
    SurvivorUpliftingContentSerializer, 
    LossUpliftingContentSerializer, 
    MentalHealthUpliftingContentSerializer, 
    IsolatedUpliftingContentSerializer)

# MOOD VIEWS
class MoodList(generics.ListCreateAPIView):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer

class MoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer

# FRONTLINE VIEWS
class FrontlineMeditationList(generics.ListCreateAPIView):
    queryset = FrontlineMeditation.objects.all()
    serializer_class = FrontlineMeditationSerializer

class FrontlineMeditationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FrontlineMeditation.objects.all()
    serializer_class = FrontlineMeditationSerializer

class FrontlineUpliftingContentList(generics.ListCreateAPIView):
    queryset = FrontlineUpliftingContent.objects.all()
    serializer_class = FrontlineUpliftingContentSerializer
    
class FrontlineUpliftingContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FrontlineUpliftingContent.objects.all()
    serializer_class = FrontlineUpliftingContentSerializer

# UNEMPLOYED VIEWS
class UnemployedMeditationList(generics.ListCreateAPIView):
    queryset = UnemployedMeditation.objects.all()
    serializer_class = UnemployedMeditationSerializer

class UnemployedMeditationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnemployedMeditation.objects.all()
    serializer_class = UnemployedMeditationSerializer

class UnemployedUpliftingContentList(generics.ListCreateAPIView):
    queryset = UnemployedUpliftingContent.objects.all()
    serializer_class = UnemployedUpliftingContentSerializer
    
class UnemployedUpliftingContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnemployedUpliftingContent.objects.all()
    serializer_class = UnemployedUpliftingContentSerializer

# SURVIVOR VIEWS
class SurvivorMeditationList(generics.ListCreateAPIView):
    queryset = SurvivorMeditation.objects.all()
    serializer_class = SurvivorMeditationSerializer

class SurvivorMeditationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SurvivorMeditation.objects.all()
    serializer_class = SurvivorMeditationSerializer

class SurvivorUpliftingContentList(generics.ListCreateAPIView):
    queryset = SurvivorUpliftingContent.objects.all()
    serializer_class = SurvivorUpliftingContentSerializer
    
class SurvivorUpliftingContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SurvivorUpliftingContent.objects.all()
    serializer_class = SurvivorUpliftingContentSerializer

# LOSS VIEWS
class LossMeditationList(generics.ListCreateAPIView):
    queryset = LossMeditation.objects.all()
    serializer_class = LossMeditationSerializer

class LossMeditationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LossMeditation.objects.all()
    serializer_class = LossMeditationSerializer

class LossUpliftingContentList(generics.ListCreateAPIView):
    queryset = LossUpliftingContent.objects.all()
    serializer_class = LossUpliftingContentSerializer
    
class LossUpliftingContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LossUpliftingContent.objects.all()
    serializer_class = LossUpliftingContentSerializer

# MENTALHEALTH VIEWS
class MentalHealthMeditationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MentalHealthMeditation.objects.all()
    serializer_class = MentalHealthMeditationSerializer

class MentalHealthMeditationList(generics.ListCreateAPIView):
    queryset = MentalHealthMeditation.objects.all()
    serializer_class = MentalHealthMeditationSerializer

class MentalHealthUpliftingContentList(generics.ListCreateAPIView):
    queryset = MentalHealthUpliftingContent.objects.all()
    serializer_class = MentalHealthUpliftingContentSerializer
    
class MentalHealthUpliftingContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MentalHealthUpliftingContent.objects.all()
    serializer_class = MentalHealthUpliftingContentSerializer

# ISOLATED VIEWS
class IsolatedMeditationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IsolatedMeditation.objects.all()
    serializer_class = IsolatedMeditationSerializer

class IsolatedMeditationList(generics.ListCreateAPIView):
    queryset = IsolatedMeditation.objects.all()
    serializer_class = IsolatedMeditationSerializer

class IsolatedUpliftingContentList(generics.ListCreateAPIView):
    queryset = IsolatedUpliftingContent.objects.all()
    serializer_class = IsolatedUpliftingContentSerializer
    
class IsolatedUpliftingContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IsolatedUpliftingContent.objects.all()
    serializer_class = IsolatedUpliftingContentSerializer