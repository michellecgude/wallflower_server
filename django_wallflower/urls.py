# project root urlpatterns
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('account/', include('users.urls')),
    path('auth/', include('djoser.urls')),

    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    path('data/', include('wallflower.urls')), 

]
