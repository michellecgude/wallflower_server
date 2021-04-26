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





#  --- USER PERSONALIZED UPLIFTING CONTENT ---
class FrontlineUpliftingContent(models.Model):

    # DATABASE FIELDS
    title = models.CharField(max_length=200, verbose_name="Article Name")
    description = models.CharField(max_length=200, verbose_name="Article Description")
    img_url = models.URLField(max_length=500, verbose_name="Image URL")
    src = models.CharField(max_length=200, verbose_name="Article Source")
    article_link = models.URLField(max_length=500, verbose_name="Article URL")

    # META
    class Meta:
        verbose_name = "Frontline User's Uplifting Content"
        verbose_name_plural = "Frontline User Uplifting Content"

    # TO STRING METHOD
    def __str__(self):
        return str(self.title) + " " + str(self.src)


class UnemployedUpliftingContent(models.Model):


    # DATABASE FIELDS
    title = models.CharField(max_length=200, verbose_name="Article Name")
    description = models.CharField(max_length=200, verbose_name="Article Description")
    img_url = models.URLField(max_length=500, verbose_name="Image URL")
    src = models.CharField(max_length=200, verbose_name="Article Source")
    article_link = models.URLField(max_length=500, verbose_name="Article URL")

    # META
    class Meta:
        verbose_name = "Unemployed User's Uplifting Content"
        verbose_name_plural = "Unemployed User Uplifting Content"

    # TO STRING METHOD
    def __str__(self):
        return str(self.title) + " " + str(self.src)

class LossUpliftingContent(models.Model):

    # DATABASE FIELDS
    title = models.CharField(max_length=200, verbose_name="Article Name")
    description = models.CharField(max_length=200, verbose_name="Article Description")
    img_url = models.URLField(max_length=500, verbose_name="Image URL")
    src = models.CharField(max_length=200, verbose_name="Article Source")
    article_link = models.URLField(max_length=500, verbose_name="Article URL")

    # META
    class Meta:
        verbose_name = "Loss User's Uplifting Content"
        verbose_name_plural = "Loss User Uplifting Content"

    # TO STRING METHOD
    def __str__(self):
        return str(self.title) + " " + str(self.src)

class MentalHealthUpliftingContent(models.Model):

    # DATABASE FIELDS
    title = models.CharField(max_length=200, verbose_name="Article Name")
    description = models.CharField(max_length=200, verbose_name="Article Description")
    img_url = models.URLField(max_length=500, verbose_name="Image URL")
    src = models.CharField(max_length=200, verbose_name="Article Source")
    article_link = models.URLField(max_length=500, verbose_name="Article URL")

    # META
    class Meta:
        verbose_name = "Mental Health's Uplifting Content"
        verbose_name_plural = "Mental Health Uplifting Content"

    # TO STRING METHOD
    def __str__(self):
        return str(self.title) + " " + str(self.src)


class IsolatedUpliftingContent(models.Model):

    # DATABASE FIELDS
    title = models.CharField(max_length=200, verbose_name="Article Name")
    description = models.CharField(max_length=200, verbose_name="Article Description")
    img_url = models.URLField(max_length=500, verbose_name="Image URL")
    src = models.CharField(max_length=200, verbose_name="Article Source")
    article_link = models.URLField(max_length=500, verbose_name="Article URL")

    # META
    class Meta:
        verbose_name = "Isolated User's Uplifting Content"
        verbose_name_plural = "Isolated User Uplifting Content"

    # TO STRING METHOD
    def __str__(self):
        return str(self.title) + " " + str(self.src)