from django.urls import include, path
from django.conf.urls import url, include

from . import views

urlpatterns = [    
    # JOURNAL URLS
    path('journals/', views.JournalList.as_view(), name="user_journal_list"),
    path('journals/<int:pk>', views.JournalDetail.as_view(), name="user_journal_detail"),

    # FRONTLINE URLS
    path('frontline-meditations/', views.FrontlineMeditationList.as_view(), name='frontline_meditation_list'),    
    path('frontline-meditations/<int:pk>', views.FrontlineMeditationDetail.as_view(), name='frontline_meditation_details'), 

    path('frontline-upliftingnews/', views.FrontlineUpliftingNewsList.as_view(), name='frontline_upliftingnews_list'),    
    path('frontline-upliftingnews/<int:pk>', views.FrontlineUpliftingNewsDetail.as_view(), name='frontline_upliftingnews_details'), 

    # UNEMPLOYED URLS   
    path('unemployed-meditations/', views.UnemployedMeditationList.as_view(), name='unemployed_meditation_list'),    
    path('unemployed-meditations/<int:pk>', views.UnemployedMeditationDetail.as_view(), name='unemployed_meditation_details'), 
    
    path('unemployed-upliftingnews/', views.UnemployedUpliftingNewsList.as_view(), name='unemployed_upliftingnews_list'),    
    path('unemployed-upliftingnews/<int:pk>', views.UnemployedUpliftingNewsDetail.as_view(), name='unemployed_upliftingnews_details'), 

    # LOSS URLS
    path('loss-meditations/', views.LossMeditationList.as_view(), name='loss_meditation_list'),    
    path('loss-meditations/<int:pk>', views.LossMeditationDetail.as_view(), name='loss_meditation_details'), 
    
    path('loss-upliftingnews/', views.LossUpliftingNewsList.as_view(), name='loss_upliftingnews_list'),    
    path('loss-upliftingnews/<int:pk>', views.LossUpliftingNewsDetail.as_view(), name='loss_upliftingnews_details'), 

    # MENTAL HEALTH URLS
    path('mentalhealth-meditations/', views.MentalHealthMeditationList.as_view(), name='mentalhealth_meditation_list'),    
    path('mentalhealth-meditations/<int:pk>', views.MentalHealthMeditationDetail.as_view(), name='mentalhealth_meditation_details'), 
    
    path('mentalhealth-upliftingnews/', views.MentalHealthUpliftingNewsList.as_view(), name='mentalhealth_upliftingnews_list'),    
    path('mentalhealth-upliftingnews/<int:pk>', views.MentalHealthUpliftingNewsDetail.as_view(), name='mentalhealth_upliftingnews_details'), 

    # ISOLATED URLS
    path('isolated-meditations/', views.IsolatedMeditationList.as_view(), name='isolated_meditation_list'),    
    path('isolated-meditations/<int:pk>', views.IsolatedMeditationDetail.as_view(), name='isolated_meditation_details'), 
    
    path('isolated-upliftingnews/', views.IsolatedUpliftingNewsList.as_view(), name='isolated_upliftingnews_list'),    
    path('isolated-upliftingnews/<int:pk>', views.IsolatedUpliftingNewsDetail.as_view(), name='isolated_upliftingnews_details'), 

]