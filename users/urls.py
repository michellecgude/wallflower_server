# app urls
from django.urls import path, include
from users import views

urlpatterns = [
  path('', views.UserListView.as_view()),
]