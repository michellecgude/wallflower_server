from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, UserProfile, Mood, Habit, Meditation, UpliftingContent
from .serializers import UserSerializer, UserSerializerWithToken, UserProfileSerializer, MoodSerializer, HabitSerializer, MeditationSerializer, UpliftingContentSerializer

@api_view(['GET'])
def current_user(request): # defining a method that determines the current user by their jwt token, reutrns their data via a http response.
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView): # creates a new user

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid(): # serializer checks if incoming data is valid, will return a create or error response depending upon input.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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