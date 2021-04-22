
from rest_framework import serializers

from .models import (
    FrontlineMeditation, 
    UnemployedMeditation, 
    LossMeditation, 
    MentalHealthMeditation, 
    IsolatedMeditation, 
    FrontlineUpliftingContent, 
    UnemployedUpliftingContent, 
    LossUpliftingContent, 
    MentalHealthUpliftingContent, 
    IsolatedUpliftingContent)

# FRONTLINE SERIALIZERS
class FrontlineMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontlineMeditation
        fields = ("id", "user", "name", "benefit", "length", "type_of_meditation", "meditation_link")

class FrontlineUpliftingContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontlineUpliftingContent
        fields = ("id", "user", "description", "img_url", "src", "article_link")


# UNEMPLOYED SERIALIZERS
class UnemployedMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnemployedMeditation
        fields = ("id", "user", "name", "benefit", "length", "type_of_meditation", "meditation_link")

class UnemployedUpliftingContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnemployedUpliftingContent
        fields = ("id", "user", "description", "img_url", "src", "article_link")

# LOSS SERIALIZERS
class LossMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LossMeditation
        fields = ("id", "user", "name", "benefit", "length", "type_of_meditation", "meditation_link")

class LossUpliftingContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LossUpliftingContent
        fields = ("id", "user", "description", "img_url", "src", "article_link")

# MENTAL HEALTH SERIALIZERS
class MentalHealthMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalHealthMeditation
        fields = ("id", "user", "name", "benefit", "length", "type_of_meditation", "meditation_link")

class MentalHealthUpliftingContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalHealthUpliftingContent
        fields = ("id", "user", "description", "img_url", "src", "article_link")

# ISOLATED SERIALIZERS
class IsolatedMeditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsolatedMeditation
        fields = ("id", "user", "name", "benefit", "length", "type_of_meditation", "meditation_link")

class IsolatedUpliftingContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsolatedUpliftingContent
        fields = ("id", "user", "description", "img_url", "src", "article_link")



