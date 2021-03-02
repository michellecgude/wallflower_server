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


class Mood(models.Model):

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_mood")

    # DATABASE FIELDS
    name = models.CharField(max_length=100, verbose_name="Mood Name")
    # mood_type = models.CharField('type', max_length=10, choices=MOOD_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Mood Log Created On")
    note_entry = models.CharField(max_length=100, verbose_name="Note On Mood Log")
    # value = models.FloatField(("")) possible feature to conditionally render frontend dash for the future...

    # META
    class Meta:
        verbose_name = "User Mood"
        verbose_name_plural = "User's Moods"

    # TO STRING METHOD
    def __str__(self):
        return "User Mood " + str(self.id) + " - " + self.name

class Habit(models.Model):

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_habit")

    # DATABASE FIELDS
    name = models.CharField(max_length=100, verbose_name="Habit Name")
    description = models.TextField(max_length=300, verbose_name="Habit Description")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Habit Created On")
    note_entry = models.CharField(max_length=100, verbose_name="Note on Habit Created")

    # META
    class Meta:
        verbose_name = "User's Habit"
        verbose_name_plural = "User's Habits"

    # TO STRING METHOD
    def __str__(self):
        return "User's Habit " + str(self.id) + " - " + self.name
    
class Meditation(models.Model):

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_meditation")

    # DATABASE FIELDS
    name = models.CharField(max_length=100, verbose_name="Meditation Name")
    purpose = models.CharField(max_length=200, verbose_name="Purpose of Meditation")
    benefit = models.CharField(max_length=200, verbose_name="Benefit")
    length = models.DurationField(verbose_name="Meditation Length")
    type_of_meditation = models.CharField(max_length=200, verbose_name="Type of Meditation")

    # META
    class Meta:
        verbose_name = "User's Meditation"
        verbose_name_plural = "User's Meditations"

    # TO STRING METHOD
    def __str__(self):
        return "User's Meditation " + str(self.id) + " - " + self.name

class UpliftingContent(models.Model):

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_uplifting_content")

    # DATABASE FIELDS
    title = models.CharField(max_length=200, verbose_name="Article Name")
    description = models.CharField(max_length=200, verbose_name="Article Description")
    img_url = models.URLField(max_length=500, verbose_name="Image URL")
    src = models.CharField(max_length=200, verbose_name="Article Source")
    article_link = models.URLField(max_length=500, verbose_name="Article URL")

    # META
    class Meta:
        verbose_name = "User's Uplifting Content"
        verbose_name_plural = "User's Uplifting Content"

    # TO STRING METHOD
    def __str__(self):
        return "User's Uplifting Content " + str(self.id) + " - " + self.title


