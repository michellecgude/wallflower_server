from rest_framework import viewsets
from rest_framework import permissions

from django.http import JsonResponse

from .models import User, UserProfile, Mood, Habit, Meditation, UpliftingContent
from .serializers import UserSerializer, UserProfileSerializer, MoodSerializer, HabitSerializer, MeditationSerializer, UpliftingContentSerializer

class UserProfileView(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = (permissions.AllowAny,)

# need this for json backend ?
# def user_profile_list(request):
#     profiles = UserProfile.objects.all().values("id", "user", "first_name", "last_name", "date_created", "role")
#     profiles_list = list(profiles)
#     return JsonResponse(user_profile_list, safe=False)


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



