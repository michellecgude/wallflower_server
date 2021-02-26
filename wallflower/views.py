from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer
from django.http import JsonResponse
from rest_framework.views import APIView

from .models import User, UserProfile, Mood, Habit, Meditation, UpliftingContent
from .serializers import UserSerializer, UserProfileSerializer, MoodSerializer, HabitSerializer, MeditationSerializer, UpliftingContentSerializer

class UserProfileView(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

class MoodView(viewsets.ModelViewSet):
    serializer_class = MoodSerializer
    queryset = Mood.objects.all()

class HabitView(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

class MeditationView(viewsets.ModelViewSet):
    serializer_class = MeditationSerializer
    queryset = Meditation.objects.all()

class UpliftingContentView(viewsets.ModelViewSet):
    serializer_class = UpliftingContentSerializer
    queryset = UpliftingContent.objects.all()















# # user auth?
# class UserProfileFormView(APIView):
#     # Assume you have a model named UserProfile
#     # And a serializer for that model named UserProfileSerializer
#     # This is the view to let users update their profile info.
#     # Like E-Mail, Birth Date etc.

#     def get_object(self, pk):
#         try:
#             return UserProfile.objects.get(pk=pk)
#         except:
#             return None

#     # this method will be called when your request is GET
#     # we will use this to fetch field names and values while creating our form on React side
#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         if not user:
#             return JsonResponse({'status': 0, 'message': 'User with this id not found'})

#         # You have a serializer that you specified which fields should be available in fo
#         serializer = UserProfileSerializer(user)
#         # And here we send it those fields to our react component as json
#         # Check this json data on React side, parse it, render it as form.
#         return JsonResponse(serializer.data, safe=False)

#     # this method will be used when user try to update or save their profile
#     # for POST requests.
#     def post(self, request, pk, format=None):
#         try:
#             user = self.get_object(pk)
