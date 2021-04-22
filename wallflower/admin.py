from django.contrib import admin

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

admin.site.register([
    FrontlineMeditation, 
    UnemployedMeditation, 
    LossMeditation, 
    MentalHealthMeditation, 
    IsolatedMeditation, 
    FrontlineUpliftingContent, 
    UnemployedUpliftingContent, 
    LossUpliftingContent, 
    MentalHealthUpliftingContent, 
    IsolatedUpliftingContent])