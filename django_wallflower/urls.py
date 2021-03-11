# project root urlpatterns
from django import urls
from django.contrib import admin
from django.urls import path, include
from . import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt import views as jwt_views

from .views import LogoutAndBlacklistRefreshTokenForUserView

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    path('auth/', include('djoser.urls')),

    path('jwtoken/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  
    path('jwtoken/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
     path('blacklistoken/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='token_blacklist'),
    
    path('data/', include('wallflower.urls')), 

]
