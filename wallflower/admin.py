from django.contrib import admin

from .models import (
    Mood, 
    Habit, 
    FrontlineMeditation, 
    UnemployedMeditation, 
    SurvivorMeditation, 
    LossMeditation, 
    MentalHealthMeditation, 
    IsolatedMeditation, 
    FrontlineUpliftingContent, 
    UnemployedUpliftingContent, 
    SurvivorUpliftingContent, 
    LossUpliftingContent, 
    MentalHealthUpliftingContent, 
    IsolatedUpliftingContent)

admin.site.register([
    Mood, 
    Habit, 
    FrontlineMeditation, 
    UnemployedMeditation, 
    SurvivorMeditation, 
    LossMeditation, 
    MentalHealthMeditation, 
    IsolatedMeditation, 
    FrontlineUpliftingContent, 
    UnemployedUpliftingContent, 
    SurvivorUpliftingContent, 
    LossUpliftingContent, 
    MentalHealthUpliftingContent, 
    IsolatedUpliftingContent])