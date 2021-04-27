from django.db import models
from users.models import User
from django.conf import settings






#  --- USER PERSONALIZED MEDITATIONS ---
class FrontlineMeditation(models.Model):

    # DATABASE FIELDS
    name = models.CharField(max_length=200, verbose_name="Meditation Name")
    description = models.TextField(max_length=200, verbose_name="Meditation Description")
    length = models.DurationField(verbose_name="Meditation Length")
    audio = models.FileField(verbose_name="Meditation Audio File")
    meditation_link = models.URLField(max_length=500, verbose_name="Meditation URL")

    # META
    class Meta:
        verbose_name = "Frontline User's Meditation"
        verbose_name_plural = "Frontline User Meditations"

    # TO STRING METHOD
    def __str__(self):
        return str(self.name) + " " + str(self.length)

class UnemployedMeditation(models.Model):

    # DATABASE FIELDS
    name = models.CharField(max_length=200, verbose_name="Meditation Name")
    description = models.TextField(max_length=200, verbose_name="Meditation Description")
    length = models.DurationField(verbose_name="Meditation Length")
    audio = models.FileField(verbose_name="Meditation Audio File")
    meditation_link = models.URLField(max_length=500, verbose_name="Meditation URL")

    # META
    class Meta:
        verbose_name = "Unemployed User's Meditation"
        verbose_name_plural = "Unemployed User Meditations"

    # TO STRING METHOD
    def __str__(self):
        return str(self.name) + " " + str(self.length)

class LossMeditation(models.Model):

    # DATABASE FIELDS
    name = models.CharField(max_length=200, verbose_name="Meditation Name")
    description = models.TextField(max_length=200, verbose_name="Meditation Description")
    length = models.DurationField(verbose_name="Meditation Length")
    audio = models.FileField(verbose_name="Meditation Audio File")
    meditation_link = models.URLField(max_length=500, verbose_name="Meditation URL")

    # META
    class Meta:
        verbose_name = "Loss User's Meditation"
        verbose_name_plural = "Loss User Meditations"

    # TO STRING METHOD
    def __str__(self):
        return str(self.name) + " " + str(self.length)

class MentalHealthMeditation(models.Model):

    # DATABASE FIELDS
    name = models.CharField(max_length=200, verbose_name="Meditation Name")
    description = models.TextField(max_length=200, verbose_name="Meditation Description")
    length = models.DurationField(verbose_name="Meditation Length")
    audio = models.FileField(verbose_name="Meditation Audio File")
    meditation_link = models.URLField(max_length=500, verbose_name="Meditation URL")

    # META
    class Meta:
        verbose_name = "Mental Health User's Meditation"
        verbose_name_plural = "Mental Health User Meditations"

    # TO STRING METHOD
    def __str__(self):
        return str(self.name) + " " + str(self.length)

class IsolatedMeditation(models.Model):

    # DATABASE FIELDS
    name = models.CharField(max_length=200, verbose_name="Meditation Name")
    description = models.TextField(max_length=200, verbose_name="Meditation Description")
    length = models.DurationField(verbose_name="Meditation Length")
    audio = models.FileField(verbose_name="Meditation Audio File")
    meditation_link = models.URLField(max_length=500, verbose_name="Meditation URL")

    # META
    class Meta:
        verbose_name = "Isolated User's Meditation"
        verbose_name_plural = "Isolated User Meditations"

    # TO STRING METHOD
    def __str__(self):
        return str(self.name) + " " + str(self.length)





#  --- USER PERSONALIZED UPLIFTING NEWS ---
class FrontlineUpliftingNews(models.Model):

    # DATABASE FIELDS
    headline = models.CharField(max_length=200, verbose_name="Headline")
    description = models.TextField(max_length=400, verbose_name="Description")
    image = models.ImageField(verbose_name="Article Image")
    author = models.CharField(max_length=150, verbose_name="Author")
    source = models.TextField(max_length=200, verbose_name="News Source")

    # META
    class Meta:
        verbose_name = "Frontline User's Uplifting News"
        verbose_name_plural = "Frontline User Uplifting News"

    # TO STRING METHOD
    def __str__(self):
        return str(self.headline) + " " + str(self.author)


class UnemployedUpliftingNews(models.Model):


    # DATABASE FIELDS
    headline = models.CharField(max_length=200, verbose_name="Headline")
    description = models.TextField(max_length=400, verbose_name="Description")
    image = models.ImageField(verbose_name="Article Image")
    author = models.CharField(max_length=150, verbose_name="Author")
    source = models.TextField(max_length=200, verbose_name="News Source")

    # META
    class Meta:
        verbose_name = "Unemployed User's Uplifting News"
        verbose_name_plural = "Unemployed User Uplifting News"

    # TO STRING METHOD
    def __str__(self):
        return str(self.headline) + " " + str(self.author)

class LossUpliftingNews(models.Model):

    # DATABASE FIELDS
    headline = models.CharField(max_length=200, verbose_name="Headline")
    description = models.TextField(max_length=400, verbose_name="Description")
    image = models.ImageField(verbose_name="Article Image")
    author = models.CharField(max_length=150, verbose_name="Author")
    source = models.TextField(max_length=200, verbose_name="News Source")

    # META
    class Meta:
        verbose_name = "Loss User's Uplifting News"
        verbose_name_plural = "Loss User Uplifting News"

    # TO STRING METHOD
    def __str__(self):
        return str(self.headline) + " " + str(self.author)

class MentalHealthUpliftingNews(models.Model):

    # DATABASE FIELDS
    headline = models.CharField(max_length=200, verbose_name="Headline")
    description = models.TextField(max_length=400, verbose_name="Description")
    image = models.ImageField(verbose_name="Article Image")
    author = models.CharField(max_length=150, verbose_name="Author")
    source = models.TextField(max_length=200, verbose_name="News Source")

    # META
    class Meta:
        verbose_name = "Mental Health's Uplifting News"
        verbose_name_plural = "Mental Health Uplifting News"

    # TO STRING METHOD
    def __str__(self):
        return str(self.headline) + " " + str(self.author)


class IsolatedUpliftingNews(models.Model):

    # DATABASE FIELDS
    headline = models.CharField(max_length=200, verbose_name="Headline")
    description = models.TextField(max_length=400, verbose_name="Description")
    image = models.ImageField(verbose_name="Article Image")
    author = models.CharField(max_length=150, verbose_name="Author")
    source = models.TextField(max_length=200, verbose_name="News Source")
    
    # META
    class Meta:
        verbose_name = "Isolated User's Uplifting News"
        verbose_name_plural = "Isolated User Uplifting News"

    # TO STRING METHOD
    def __str__(self):
        return str(self.headline) + " " + str(self.author)