# project root urlpatterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('usersapi/', include('usersapi.urls')),
    path('userdata/', include('wallflower.urls')), # includes app's urlpatterns

]
