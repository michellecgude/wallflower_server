
from rest_framework import serializers

from .models import (
    Journal,
    FrontlineMeditation, 
    UnemployedMeditation, 
    LossMeditation, 
    MentalHealthMeditation, 
    IsolatedMeditation, 
    FrontlineUpliftingNews, 
    UnemployedUpliftingNews, 
    LossUpliftingNews, 
    MentalHealthUpliftingNews, 
    IsolatedUpliftingNews)


# JOURNAL SERIALIZERS
class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ("id", "user", "journal_title", "journal_bodytext")

# FRONTLINE SERIALIZERS
class FrontlineMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontlineMeditation
        fields = ("name", "description", "length", "audio", "meditation_link")

class FrontlineUpliftingNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontlineUpliftingNews
        fields = ("headline", "description", "image", "author", "source")


# UNEMPLOYED SERIALIZERS
class UnemployedMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnemployedMeditation
        fields = ("name", "description", "length", "audio", "meditation_link")

class UnemployedUpliftingNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnemployedUpliftingNews
        fields = ("headline", "description", "image", "author", "source")

# LOSS SERIALIZERS
class LossMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LossMeditation
        fields = ("name", "description", "length", "audio", "meditation_link")

class LossUpliftingNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LossUpliftingNews
        fields = ("headline", "description", "image", "author", "source")

# MENTAL HEALTH SERIALIZERS
class MentalHealthMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalHealthMeditation
        fields = ("name", "description", "length", "audio", "meditation_link")

class MentalHealthUpliftingNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalHealthUpliftingNews
        fields = ("headline", "description", "image", "author", "source")

# ISOLATED SERIALIZERS
class IsolatedMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsolatedMeditation
        fields = ("name", "description", "length", "audio", "meditation_link")

class IsolatedUpliftingNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsolatedUpliftingNews
        fields = ("headline", "description", "image", "author", "source")



