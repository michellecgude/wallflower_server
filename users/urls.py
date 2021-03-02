# app urls
from django.urls import path, include
from users import views
from . import views

urlpatterns = [

   # USER PROFILES
    path('userprofiles/', views.UserProfileList.as_view(), name='userprofile_list'),    
    path('userprofiles/<int:pk>', views.UserProfileDetail.as_view(), name='userprofile_details'),   
  path('', views.UserListView.as_view()),
]