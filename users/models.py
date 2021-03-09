from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

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

    # CHOICES
    DEMOGRAPHIC_CHOICES = (
        ('frontline healthcare user', 'Frontline Healthcare User'),
        ('unemployed user', 'Unemployed User'),
        ('covid survivor user', 'COVID Survivor User'),
        ('loss of loved one user', 'Loss of Loved One User'),
        ('pre existing mental health user', 'Pre Existing Mental Health User'),
        ('socially isolated user', 'Socially Isolated User')
    )


    # RELATIONSHIP
    # user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True, on_delete=models.CASCADE)
    
    # DATABASE FIELDS
    date_created = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Profile Created On", null=True)
    role = models.CharField(max_length=255, verbose_name="User Demographic", choices=DEMOGRAPHIC_CHOICES, null=True)

    # DEFINING FUNCTION FOR USER = PROFILE FIELDS, AUTO CREATION
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
            
    post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)

# simplebetterthancomplex option ???
    # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    # def create_or_update_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         UserProfile.objects.create(user=instance)
    #     instance.profile.save()

    # META
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    # TO STRING METHOD
    def __str__(self):
        return self.user.email