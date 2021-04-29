from django.db.models import query
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (Journal)

from .serializers import (JournalSerializer)

# JOURNAL VIEWS
class JournalList(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer