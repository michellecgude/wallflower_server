from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class User(AbstractUser):
# auth/login related fields for user, extending user class.
    name = models.CharField((""), max_length=100)
    email = models.EmailField((""), max_length=254)
    password = models.CharField((""), max_length=85)

    # one to one field user, title : charfield,
    # foreign key = user_id

class Profile(models.Model):
# non-auth-related/cosmetic fields go here.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)



class Mood(models.Model):
	name = models.CharField((""), max_length=100)
	timestamp = models.TimeField((""), auto_now=False, auto_now_add=False)
	notes = models.TextField((""))

class Meditation(models.Model):
	title = models.CharField((""), max_length=255)
	length = models.CharField((""), max_length=50)
	description = models.TextField((""), max_length=500)
	purpose = models.TextField((""), max_length=500)
	audio = models.URLField((""), max_length=200)
	notes = models.TextField((""))

class UpliftingContent(models.Model):
	title = models.TextField((""), max_length=500)
	description = models.TextField((""), max_length=500)
	img = models.URLField((""), max_length=200)
	link = models.URLField((""), max_length=200)
	notes = models.TextField((""))


