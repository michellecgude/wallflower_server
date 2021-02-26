# app urls / #mysite

from django.urls import include, path
from django.conf.urls import url, include
from django.contrib.auth.urls import views as auth_views

urlpatterns = [

    path('auth/', include('rest_auth.urls')),    
    path('auth/register/', include('rest_auth.registration.urls'))
]