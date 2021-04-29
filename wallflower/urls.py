from django.urls import include, path
from django.conf.urls import url, include

from . import views

urlpatterns = [    
    # JOURNAL URLS
    path('journals/', views.JournalList.as_view(), name="user_journal_list"),
    path('journals/<int:pk>', views.JournalDetail.as_view(), name="user_journal_detail"),
]