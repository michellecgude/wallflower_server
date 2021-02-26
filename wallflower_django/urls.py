# backend urls

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from wallflower import views

router = routers.DefaultRouter()
router.register(r'userprofiles', views.UserProfileView, 'userprofile')
router.register(r'moods', views.MoodView, 'mood')
router.register(r'habits', views.HabitView, 'habit')
router.register(r'meditations', views.MeditationView, 'meditation')
router.register(r'upliftingcontents', views.UpliftingContentView, 'upliftingcontent')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/v1/wallflowerusers/', include('wallflower.urls')),

    # changing it to json?
    # path('userprofilejson/', views.user_profile_list.as_view(), name='profiles_list')

]