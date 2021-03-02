from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):  # auth/login-related fields
    
    # DATABASE FIELDS
    email = models.EmailField(("email address"), unique=True) # changes email to unique, blank to false.
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    # META
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    # TO STRING METHOD
    def __str__(self):
        return "User " + str(self.id) + " - " + self.email

class UserProfile(models.Model):  # non-auth related/cosmetic fields

    # RELATIONSHIP
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    
    # DATABASE FIELDS
    # dob = models.DateField(auto_now=False, auto_now_add=False) possible date of birth entry for the future...
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    date_created = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Profile Created On")
    role = models.CharField(max_length=255, verbose_name="User Demographic")
    # roles ? = frontline healthcare, unemployed, covid survivor + sick, loss of loved one, mentally ill, socially isolated user

    # META
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    # TO STRING METHOD
    def __str__(self):
        return self.first_name