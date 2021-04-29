
from rest_framework import serializers

from .models import (Journal)


# JOURNAL SERIALIZERS
class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ("id", "user", "title", "body", "date_created")

