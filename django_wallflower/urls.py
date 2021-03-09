# project root urlpatterns
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('account/', include('users.urls')),
    path('auth/', include('djoser.urls')),

    path('jwtoken/obtain/', TokenObtainPairView.as_view(), name='token_create'),  
    path('jwtoken/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('data/', include('wallflower.urls')), 

]
