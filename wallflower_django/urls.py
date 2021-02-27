# backend urls

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from wallflower import views

router = routers.DefaultRouter()
router.register(r'userprofiles', views.UserProfileView, 'userprofile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wallflower.urls')),
    path('api/v1/wallflowerusers/', include('wallflower.urls')),
]