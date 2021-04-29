from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# --- CUSTOM USER ---
class User(AbstractUser): 

     # CHOICES
    DEMOGRAPHIC_CHOICES = (
        ('frontline', 'Frontline Healthcare Worker'),
        ('unemployed', 'Unemployed'),
        ('bereaving', 'Lost a Loved One'),
        ('sick', 'Sick with COVID/Or had been'),
        ('mentalhealth', 'Pre Existing Mental Health Issues'),
        ('lonely', 'Lonely')
    )
    
    # AUTH FIELDS
    email = models.EmailField(("email address"), unique=True) 
    # NON AUTH FIELDS
    role = models.CharField(max_length=255, verbose_name="User Demographic", choices=DEMOGRAPHIC_CHOICES)
    
    REQUIRED_FIELDS = ['first_name','last_name', 'username', 'role']
    USERNAME_FIELD = 'email'
    
    # META
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    # TO STRING METHOD
    def __str__(self):
        return str(self.first_name) + str(self.id)