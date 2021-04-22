from django.urls import include, path
from django.conf.urls import url, include

from . import views

urlpatterns = [    
    # FRONTLINE URLS
    path('frontline-meditations/', views.FrontlineMeditationList.as_view(), name='frontline_meditation_list'),    
    path('frontline-meditations/<int:pk>', views.FrontlineMeditationDetail.as_view(), name='frontline_meditation_details'), 

    path('frontline-upliftingcontents/', views.FrontlineUpliftingContentList.as_view(), name='frontline_upliftingcontent_list'),    
    path('frontline-upliftingcontents/<int:pk>', views.FrontlineUpliftingContentDetail.as_view(), name='frontline_upliftingcontent_details'), 

    # UNEMPLOYED URLS   
    path('unemployed-meditations/', views.UnemployedMeditationList.as_view(), name='unemployed_meditation_list'),    
    path('unemployed-meditations/<int:pk>', views.UnemployedMeditationDetail.as_view(), name='unemployed_meditation_details'), 
    
    path('unemployed-upliftingcontents/', views.UnemployedUpliftingContentList.as_view(), name='unemployed_upliftingcontent_list'),    
    path('unemployed-upliftingcontents/<int:pk>', views.UnemployedUpliftingContentDetail.as_view(), name='unemployed_upliftingcontent_details'), 

    # LOSS URLS
    path('loss-meditations/', views.LossMeditationList.as_view(), name='loss_meditation_list'),    
    path('loss-meditations/<int:pk>', views.LossMeditationDetail.as_view(), name='loss_meditation_details'), 
    
    path('loss-upliftingcontents/', views.LossUpliftingContentList.as_view(), name='loss_upliftingcontent_list'),    
    path('loss-upliftingcontents/<int:pk>', views.LossUpliftingContentDetail.as_view(), name='loss_upliftingcontent_details'), 

    # MENTAL HEALTH URLS
    path('mentalhealth-meditations/', views.MentalHealthMeditationList.as_view(), name='mentalhealth_meditation_list'),    
    path('mentalhealth-meditations/<int:pk>', views.MentalHealthMeditationDetail.as_view(), name='mentalhealth_meditation_details'), 
    
    path('mentalhealth-upliftingcontents/', views.MentalHealthUpliftingContentList.as_view(), name='mentalhealth_upliftingcontent_list'),    
    path('mentalhealth-upliftingcontents/<int:pk>', views.MentalHealthUpliftingContentDetail.as_view(), name='mentalhealth_upliftingcontent_details'), 

    # ISOLATED URLS
    path('isolated-meditations/', views.IsolatedMeditationList.as_view(), name='isolated_meditation_list'),    
    path('isolated-meditations/<int:pk>', views.IsolatedMeditationDetail.as_view(), name='isolated_meditation_details'), 
    
    path('isolated-upliftingcontents/', views.IsolatedUpliftingContentList.as_view(), name='isolated_upliftingcontent_list'),    
    path('isolated-upliftingcontents/<int:pk>', views.IsolatedUpliftingContentDetail.as_view(), name='isolated_upliftingcontent_details'), 

]