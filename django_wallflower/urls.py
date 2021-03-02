# project root urlpatterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),

    # path('', include('wallflower.urls')), # includes app's urlpatterns
    path('users/', include('users.urls')) # includes app's urlpatterns

]
