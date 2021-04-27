from django.contrib import admin

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

admin.site.register([
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
    IsolatedUpliftingNews])