# A URL mapper. This file allows the request to be sent to the correct view.
# It defines a list of mappings between routes (specific URL patterns) and corresponding view functions.
# If an HTTP Request is received that has a URL matching a specific pattern, then the associated view function will be called and passed the request. 

from django.contrib import admin
from django.urls import include, path

# urlpatterns is an object that has a list with a path() and/or re_path() functions.
# path() and re_path() take two arguments.
#   1) The first is the route that will be matched. Angle brackets are used to define parts of the URL that will
#      be captured and passed through the view function as named arguments.
#   2) The second is another function that will be called when the pattern is matched. The funcion is defined with name='{corresponding view function...}'.
        # Between these two arguments is where the function can be found in the view file.

# The re_path function uses flexible pattern matching known as "regular expression" (discuss later.)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/wallflowerusers/', include('wallflower.urls')),
]
