
from rest_framework import serializers

from .models import (
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

# FRONTLINE SERIALIZERS
class FrontlineMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontlineMeditation
        fields = ("id", "user", "name", "benefit", "length", "type_of_meditation", "meditation_link")

class FrontlineUpliftingNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontlineUpliftingNews
        fields = ("id", "user", "description", "img_url", "src", "article_link")


# UNEMPLOYED SERIALIZERS
class UnemployedMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnemployedMeditation
        fields = ("id", "user", "name", "benefit", "length", "type_of_meditation", "meditation_link")

class UnemployedUpliftingNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnemployedUpliftingNews
        fields = ("id", "user", "description", "img_url", "src", "article_link")

# LOSS SERIALIZERS
class LossMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LossMeditation
        fields = ("id", "user", "name", "benefit", "length", "type_of_meditation", "meditation_link")

class LossUpliftingNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LossUpliftingNews
        fields = ("id", "user", "description", "img_url", "src", "article_link")

# MENTAL HEALTH SERIALIZERS
class MentalHealthMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalHealthMeditation
        fields = ("id", "user", "name", "benefit", "length", "type_of_meditation", "meditation_link")

class MentalHealthUpliftingNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalHealthUpliftingNews
        fields = ("id", "user", "description", "img_url", "src", "article_link")

# ISOLATED SERIALIZERS
class IsolatedMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsolatedMeditation
        fields = ("id", "user", "name", "benefit", "length", "type_of_meditation", "meditation_link")

class IsolatedUpliftingNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsolatedUpliftingNews
        fields = ("id", "user", "description", "img_url", "src", "article_link")



