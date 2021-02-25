from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# IMPORTANT NOTE WHEN PASSING USER:
# When you define a foreign key or many-to-many relations to the User model, you should specify the custom model using the AUTH_USER_MODEL setting. Like so:
# User = models.ForeignKey(settings.AUTH_USER_MODEL)

class User(AbstractUser):  # auth/login-related fields
    
    # DATABASE FIELDS
    USERNAME_FIELD = 'username'
    email = models.EmailField(("email address"), unique=True) # changes email to unique, blank to false.
    REQUIRED_FIELDS = ['email']
    # examples:
    # email (if used for login)
    # extra permissions


class UserProfile(models.Model):  # non-auth related/cosmetic fields

    # DATABASE FIELDS
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # dob = models.DateField(auto_now=False, auto_now_add=False) possible date of birth entry for the future...
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=False, auto_now_add=False)
    # roles ? = frontline healthcare, unemployed, covid survivor + sick, loss of loved one, mentally ill, socially isolated user

    # TO STRING METHOD
    def __str__(self):
        return self.user

class Mood(models.Model):
    # HAPPY = 'HAPPY'
    # COMFORTABLE = 'COMFORTABLE'
    # CALM = 'CALM'
    # CONTENT = 'CONTENT'
    # NEUTRAL = 'NEUTRAL'
    # ANXIOUS = 'ANXIOUS'
    # SAD = 'SAD'
    # STRESSED = 'STRESSED'
    # OVERWHELMED = 'OVERWHELMED'
    # TIRED = 'TIRED'
    # MOOD_TYPE_CHOICES = (
    #     (HAPPY, 'Happy')
    #     (COMFORTABLE, 'Comfortable')
    #     (CALM, 'Calm')
    #     (CONTENT, 'Content')
    #     (NEUTRAL, 'Neutral')
    #     (ANXIOUS, 'Anxious')
    #     (SAD, 'Sad')
    #     (STRESSED, 'Stressed')
    #     (OVERWHELMED, 'Overwhelmed')
    #     (TIRED, 'Tired')
    # )

    # DATABASE FIELDS
    name = models.CharField(max_length=100)
    # mood_type = models.CharField('type', max_length=10, choices=MOOD_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    note_entry = models.CharField(max_length=100)
    # value = models.FloatField(("")) possible feature to conditionally render frontend dash for the future...


    # TO STRING METHOD
    def __str__(self):
        return self.name

class Habit(models.Model):

    # DATABASE FIELDS
    name = models.CharField(max_length=100)
    description = models.TextField((""), max_length=300)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    note_entry = models.CharField(max_length=100)

    # TO STRING METHOD
    def __str__(self):
        return self.name
    
class Meditation(models.Model):

    # DATABASE FIELDS
    name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=200)
    benefit = models.CharField(max_length=200)
    length = models.DurationField((""))
    type_of_meditation = models.CharField(max_length=200)

    # TO STRING METHOD
    def __str__(self):
        return self.name

class UpliftingContent(models.Model):

    # DATABASE FIELDS
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    img_url = models.URLField(max_length=500)
    src_link = models.URLField(max_length=500)
    article_link = models.URLField(max_length=500)

    # TO STRING METHOD
    def __str__(self):
        return self.title






# Create your models here.
# A model is the single, definitive source of information about your data.
# It contains the essential fields and behaviors of the data you’re storing.
# Generally, each model maps to a single database table.

# In summary, models are python objects that define the structure of an applications data,
# and provide mechanisms to manage (add, modify, delete) and query records to in the database.

# Django in particular uses models to manage and query the data.
# Models are extensive in nature. They define the structure of stored data... This includes:
#    Field types (and possily maximum size), Default values, selection list options, help text for doc, label text for forms, etc. 
# The definition of the model is independent of the underlying database
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction#defining_data_models_models.py

# Before you jump in and start coding the models, it's worth taking a few minutes to think about what data we need to store and
# the relationships between the different objects.

# We know that we need to store information about books (title, summary, author, written language, category, ISBN) and that we
# might have multiple copies available (with globally unique id, availability status, etc.). We might need to store more information
# about the author than just their name, and there might be multiple authors with the same or similar names.
# We want to be able to sort information based on book title, author, written language, and category.

# When designing your models it makes sense to have separate models for every "object" (a group of related information).
# In this case, the obvious objects are books, book instances, and authors.

# You might also want to use models to represent selection-list options (e.g. like a drop down list of choices), rather than hard coding
# the choices into the website itself — this is recommended when all the options aren't known up front or may change.
# Obvious candidates for models, in this case, include the book genre (e.g. Science Fiction, French Poetry, etc.) and language (English, French, Japanese).

# Once we've decided on our models and field, we need to think about the relationships.
# Django allows you to define relationships that are one to one (OneToOneField), one to many (ForeignKey) and many to many (ManyToManyField).

# RELATIONSHIPS IN DJANGO:
# PARENT - CHILD RELATIONSHIP :: ONE-TO-MANY OR MANY-TO-ONE
# TABLE THAT REPRESENTS A PARENT, HAS MANY CHILDREN (IE, FIELDS), BUT EACH CHILD CAN ONLY HAVE ONE PARENT.
# WHEN USING FOREIGN KEYS, PUT THEM ON THE CHILD MODEL BECAUSE IT ONLY HAS ONE PARENT, NAME IT AFTER THE PARENT.
# FOREIGN KEYS REFERENCE ANOTHER TABLE(IE, MODEL)

# MANY TO MANY :: MOVIES + CHARACTERS IN MOVIES FOR EXAMPLE.
# WITH MANY TO MANY, YOU SHOULD PUT THE RELATIONSHIP ON A LOWER LEVEL TABLE (OR LOWER STATUS)



