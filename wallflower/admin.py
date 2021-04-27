from django.contrib import admin

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

admin.site.register([
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