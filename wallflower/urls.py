from django.urls import include, path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    # view paths:
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