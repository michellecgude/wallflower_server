from django.db import models
from users.models import User
from django.conf import settings


class Mood(models.Model):

    # CHOICES
    MOOD_TYPE_CHOICES = (
    ('happy', 'Happy'),
    ('comfortable', 'Comfortable'),
    ('calm', 'Calm'),
    ('content', 'Content'),
    ('neutral', 'Neutral'),
    ('anxious', 'Anxious'),
    ('sad', 'Sad'),
    ('stressed', 'Stressed'),
    ('overwhelmed', 'Overwhelmed'),
    ('tired', 'Tired')
)

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_mood")

    # DATABASE FIELDS
    mood_type = models.CharField('type', max_length=30, choices=MOOD_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Mood Log Created On")
    note_entry = models.CharField(max_length=100, verbose_name="Note On Mood Log", blank=True)

    # META
    class Meta:
        verbose_name = "User Mood"
        verbose_name_plural = "User Moods"

    # TO STRING METHOD
    def __str__(self):
        return "User Mood " + str(self.id) + " - " + self.mood_type

class Habit(models.Model):

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_habit")

    # DATABASE FIELDS
    name = models.CharField(max_length=100, verbose_name="Habit Name")
    description = models.TextField(max_length=300, verbose_name="Habit Description", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Habit Created On")
    note_entry = models.CharField(max_length=100, verbose_name="Note on Habit Created", blank=True)

    # META
    class Meta:
        verbose_name = "User's Habit"
        verbose_name_plural = "User Habits"

    # TO STRING METHOD
    def __str__(self):
        return "User's Habit " + str(self.id) + " - " + self.name
    
class Meditation(models.Model):

    # CHOICES
    BENEFIT_CHOICES = (
    ('happiness', 'Happiness'),
    ('acceptance', 'Acceptance'),
    ('resilience', 'Resilience'),
    ('relaxation', 'Relaxation'),
    ('letting go', 'Letting Go'),
    ('depression', 'Depression'),
    ('anxiety', 'Anxiety'),
    ('stress', 'Stress'),
    ('grief', 'Grief'),
    ('healing', 'Healing'),
    ('workplace', 'Workplace'),
    ('sleep', 'Sleep'),
    ('gratitude', 'Gratitude'),
    ('body scan', 'Body Scan')
)

    MEDITATION_TYPE_CHOICES = (
    ('guided', 'Guided'),
    ('unguided', 'Unguided'),
)

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_meditation")

    # DATABASE FIELDS
    name = models.CharField(max_length=100, verbose_name="Meditation Name")
    benefit = models.CharField(max_length=200, verbose_name="Benefit", choices=BENEFIT_CHOICES)
    length = models.DurationField(verbose_name="Meditation Length")
    type_of_meditation = models.CharField(max_length=200, verbose_name="Type of Meditation", choices=MEDITATION_TYPE_CHOICES)
    meditation_link = models.URLField(max_length=500, verbose_name="Meditation URL")

    # META
    class Meta:
        verbose_name = "User's Meditation"
        verbose_name_plural = "User Meditations"

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
        verbose_name_plural = "User Uplifting Content"

    # TO STRING METHOD
    def __str__(self):
        return "User's Uplifting Content " + str(self.id) + " - " + self.title


