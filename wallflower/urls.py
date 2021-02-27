# app urls / #mysite

from django.urls import include, path
from django.conf.urls import url, include
from django.contrib.auth.urls import views as auth_views

from . import views
from .views import current_user, UserList
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # AUTH & TOKEN URLS
    path('auth/', include('rest_auth.urls')),    
    path('auth/register/', include('rest_auth.registration.urls')),
    path('token-auth/', obtain_jwt_token),  # allows token login.


    # view paths:
    # USER AUTH (LOGIN/SIGNUP)
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    # USER PROFILES
    path('userprofiles/', views.UserProfileList.as_view(), name='userprofile_list'),    
    path('userprofiles/<int:pk>', views.UserProfileDetail.as_view(), name='userprofile_details'),   
    # MOODS
    path('moods/', views.MoodList.as_view(), name='mood_list'),    
    path('moods/<int:pk>', views.MoodDetail.as_view(), name='mood_details'),    
    # HABITS
    path('habits/', views.HabitList.as_view(), name='habit_list'),    
    path('habits/<int:pk>', views.HabitDetail.as_view(), name='habit_details'),    
    # MEDITATIONS
    path('meditations/', views.MeditationList.as_view(), name='meditation_list'),    
    path('meditations/<int:pk>', views.MeditationDetail.as_view(), name='meditation_details'),    
    # UPLIFTING CONTENTS
    path('upliftingcontent/', views.UpliftingContentList.as_view(), name='upliftingcontent_list'),    
    path('upliftingcontent/<int:pk>', views.UpliftingContentDetail.as_view(), name='upliftingcontent_details')    

]