from django.shortcuts import render
from django.http import HttpResponse
from .models import User, UserProfile, Mood, Habit, Meditation, UpliftingContent

# Create your views here.



# Views are "request handler functions". They recieve HTTP requests and return HTTP responses.
# Views access the data needed to satisfy requests via models and delegate the formatting of the response to templates.

# In full, views are the heart of the application. In between recieving and sending HTTP requests,
# they also marshall other resources of the framework to access databases, render templates, etc.

# Like all view functions, it receives an HttpRequest object as a param (request), and returns an HttpResponse.
# Here's an example of such:
# def index(request):
#     # Get an HttpRequest - the request parameter
#     # perform operations using information from the request.
#     # Return HttpResponse
#     return HttpResponse('Hello from Django!')

# Querying the data in views.py is how the Djando model communicates with views by providing a simple query API for searching the associated database.
# These queries can match against a number of fields at a time using different criteria and can support complex statements (for example, you can specify
# a search that a specific model have a field that starts with or ends with, etc.)
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction#querying_data_views.py
