from django.db.models import query
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    Journal,
    FrontlineMeditation, 
    UnemployedMeditation, 
    LossMeditation, 
    MentalHealthMeditation, 
    IsolatedMeditation, 
    FrontlineUpliftingNews, 
    UnemployedUpliftingNews, 
    LossUpliftingNews, 
    MentalHealthUpliftingNews, 
    IsolatedUpliftingNews)

from .serializers import (
    JournalSerializer,
    FrontlineMeditationSerializer, 
    UnemployedMeditationSerializer, 
    LossMeditationSerializer, 
    MentalHealthMeditationSerializer, 
    IsolatedMeditationSerializer, 
    FrontlineUpliftingNewsSerializer, 
    UnemployedUpliftingNewsSerializer, 
    LossUpliftingNewsSerializer, 
    MentalHealthUpliftingNewsSerializer, 
    IsolatedUpliftingNewsSerializer)

# JOURNAL VIEWS
class JournalList(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

# FRONTLINE VIEWS
class FrontlineMeditationList(generics.ListCreateAPIView):
    queryset = FrontlineMeditation.objects.all()
    serializer_class = FrontlineMeditationSerializer

class FrontlineMeditationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FrontlineMeditation.objects.all()
    serializer_class = FrontlineMeditationSerializer

class FrontlineUpliftingNewsList(generics.ListCreateAPIView):
    queryset = FrontlineUpliftingNews.objects.all()
    serializer_class = FrontlineUpliftingNewsSerializer
    
class FrontlineUpliftingNewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FrontlineUpliftingNews.objects.all()
    serializer_class = FrontlineUpliftingNewsSerializer

# UNEMPLOYED VIEWS
class UnemployedMeditationList(generics.ListCreateAPIView):
    queryset = UnemployedMeditation.objects.all()
    serializer_class = UnemployedMeditationSerializer

class UnemployedMeditationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnemployedMeditation.objects.all()
    serializer_class = UnemployedMeditationSerializer

class UnemployedUpliftingNewsList(generics.ListCreateAPIView):
    queryset = UnemployedUpliftingNews.objects.all()
    serializer_class = UnemployedUpliftingNewsSerializer
    
class UnemployedUpliftingNewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnemployedUpliftingNews.objects.all()
    serializer_class = UnemployedUpliftingNewsSerializer

# LOSS VIEWS
class LossMeditationList(generics.ListCreateAPIView):
    queryset = LossMeditation.objects.all()
    serializer_class = LossMeditationSerializer

class LossMeditationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LossMeditation.objects.all()
    serializer_class = LossMeditationSerializer

class LossUpliftingNewsList(generics.ListCreateAPIView):
    queryset = LossUpliftingNews.objects.all()
    serializer_class = LossUpliftingNewsSerializer
    
class LossUpliftingNewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LossUpliftingNews.objects.all()
    serializer_class = LossUpliftingNewsSerializer

# MENTALHEALTH VIEWS
class MentalHealthMeditationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MentalHealthMeditation.objects.all()
    serializer_class = MentalHealthMeditationSerializer

class MentalHealthMeditationList(generics.ListCreateAPIView):
    queryset = MentalHealthMeditation.objects.all()
    serializer_class = MentalHealthMeditationSerializer

class MentalHealthUpliftingNewsList(generics.ListCreateAPIView):
    queryset = MentalHealthUpliftingNews.objects.all()
    serializer_class = MentalHealthUpliftingNewsSerializer
    
class MentalHealthUpliftingNewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MentalHealthUpliftingNews.objects.all()
    serializer_class = MentalHealthUpliftingNewsSerializer

# ISOLATED VIEWS
class IsolatedMeditationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IsolatedMeditation.objects.all()
    serializer_class = IsolatedMeditationSerializer

class IsolatedMeditationList(generics.ListCreateAPIView):
    queryset = IsolatedMeditation.objects.all()
    serializer_class = IsolatedMeditationSerializer

class IsolatedUpliftingNewsList(generics.ListCreateAPIView):
    queryset = IsolatedUpliftingNews.objects.all()
    serializer_class = IsolatedUpliftingNewsSerializer
    
class IsolatedUpliftingNewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IsolatedUpliftingNews.objects.all()
    serializer_class = IsolatedUpliftingNewsSerializer