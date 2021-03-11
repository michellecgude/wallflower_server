from django.db import models
from users.models import User
from django.conf import settings





#  --- MOODS ---
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
        return "User's Mood " + str(self.user.first_name) + str(self.user.role) + " - " + self.name





#  --- HABITS ---
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
        return "User's Habit " + str(self.user.first_name) + str(self.user.role) + " - " + self.name
    




#  --- USER PERSONALIZED MEDITATIONS ---
class FrontlineMeditation(models.Model):

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="frontline_meditation", blank=True)

    # DATABASE FIELDS
    name = models.CharField(max_length=100, verbose_name="Meditation Name")
    benefit = models.CharField(max_length=200, verbose_name="Benefit", choices=BENEFIT_CHOICES)
    length = models.DurationField(verbose_name="Meditation Length")
    type_of_meditation = models.CharField(max_length=200, verbose_name="Type of Meditation", choices=MEDITATION_TYPE_CHOICES)
    meditation_link = models.URLField(max_length=500, verbose_name="Meditation URL")

    # META
    class Meta:
        verbose_name = "Frontline User's Meditation"
        verbose_name_plural = "Frontline User Meditations"

    # TO STRING METHOD
    def __str__(self):
        return "Frontline User's Meditation " + str(self.user.first_name) + str(self.user.role) + " - " + self.name

class UnemployedMeditation(models.Model):

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="unemployed_meditation", blank=True)

    # DATABASE FIELDS
    name = models.CharField(max_length=100, verbose_name="Meditation Name")
    benefit = models.CharField(max_length=200, verbose_name="Benefit", choices=BENEFIT_CHOICES)
    length = models.DurationField(verbose_name="Meditation Length")
    type_of_meditation = models.CharField(max_length=200, verbose_name="Type of Meditation", choices=MEDITATION_TYPE_CHOICES)
    meditation_link = models.URLField(max_length=500, verbose_name="Meditation URL")

    # META
    class Meta:
        verbose_name = "Unemployed User's Meditation"
        verbose_name_plural = "Unemployed User Meditations"

    # TO STRING METHOD
    def __str__(self):
        return "Unemployed User's Meditation " + str(self.user.first_name) + str(self.user.role) + " - " + self.name

class SurvivorMeditation(models.Model):

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
    ('sleep', 'Sleep'),
    ('gratitude', 'Gratitude'),
    ('body scan', 'Body Scan')
)

    MEDITATION_TYPE_CHOICES = (
    ('guided', 'Guided'),
    ('unguided', 'Unguided'),
)

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="survivor_meditation", blank=True)

    # DATABASE FIELDS
    name = models.CharField(max_length=100, verbose_name="Meditation Name")
    benefit = models.CharField(max_length=200, verbose_name="Benefit", choices=BENEFIT_CHOICES)
    length = models.DurationField(verbose_name="Meditation Length")
    type_of_meditation = models.CharField(max_length=200, verbose_name="Type of Meditation", choices=MEDITATION_TYPE_CHOICES)
    meditation_link = models.URLField(max_length=500, verbose_name="Meditation URL")

    # META
    class Meta:
        verbose_name = "Survivor User's Meditation"
        verbose_name_plural = "Survivor User Meditations"

    # TO STRING METHOD
    def __str__(self):
        return "Survivor User's Meditation " + str(self.user.first_name) + str(self.user.role) + " - " + self.name

class LossMeditation(models.Model):

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
    ('sleep', 'Sleep'),
    ('gratitude', 'Gratitude'),
    ('body scan', 'Body Scan')
)

    MEDITATION_TYPE_CHOICES = (
    ('guided', 'Guided'),
    ('unguided', 'Unguided'),
)

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="loss_meditation", blank=True)

    # DATABASE FIELDS
    name = models.CharField(max_length=100, verbose_name="Meditation Name")
    benefit = models.CharField(max_length=200, verbose_name="Benefit", choices=BENEFIT_CHOICES)
    length = models.DurationField(verbose_name="Meditation Length")
    type_of_meditation = models.CharField(max_length=200, verbose_name="Type of Meditation", choices=MEDITATION_TYPE_CHOICES)
    meditation_link = models.URLField(max_length=500, verbose_name="Meditation URL")

    # META
    class Meta:
        verbose_name = "Loss User's Meditation"
        verbose_name_plural = "Loss User Meditations"

    # TO STRING METHOD
    def __str__(self):
        return "Loss User's Meditation " + str(self.user.first_name) + str(self.user.role) + " - " + self.name

class MentalHealthMeditation(models.Model):

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
    ('sleep', 'Sleep'),
    ('gratitude', 'Gratitude'),
    ('body scan', 'Body Scan')
)

    MEDITATION_TYPE_CHOICES = (
    ('guided', 'Guided'),
    ('unguided', 'Unguided'),
)

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mentalhealth_meditation", blank=True)

    # DATABASE FIELDS
    name = models.CharField(max_length=100, verbose_name="Meditation Name")
    benefit = models.CharField(max_length=200, verbose_name="Benefit", choices=BENEFIT_CHOICES)
    length = models.DurationField(verbose_name="Meditation Length")
    type_of_meditation = models.CharField(max_length=200, verbose_name="Type of Meditation", choices=MEDITATION_TYPE_CHOICES)
    meditation_link = models.URLField(max_length=500, verbose_name="Meditation URL")

    # META
    class Meta:
        verbose_name = "Mental Health User's Meditation"
        verbose_name_plural = "Mental Health User Meditations"

    # TO STRING METHOD
    def __str__(self):
        return "Mental Health User's Meditation " + str(self.user.first_name) + str(self.user.role) + " - " + self.name

class IsolatedMeditation(models.Model):

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
    ('sleep', 'Sleep'),
    ('gratitude', 'Gratitude'),
    ('body scan', 'Body Scan')
)

    MEDITATION_TYPE_CHOICES = (
    ('guided', 'Guided'),
    ('unguided', 'Unguided'),
)

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="isolated_meditation", blank=True)

    # DATABASE FIELDS
    name = models.CharField(max_length=100, verbose_name="Meditation Name")
    benefit = models.CharField(max_length=200, verbose_name="Benefit", choices=BENEFIT_CHOICES)
    length = models.DurationField(verbose_name="Meditation Length")
    type_of_meditation = models.CharField(max_length=200, verbose_name="Type of Meditation", choices=MEDITATION_TYPE_CHOICES)
    meditation_link = models.URLField(max_length=500, verbose_name="Meditation URL")

    # META
    class Meta:
        verbose_name = "Isolated User's Meditation"
        verbose_name_plural = "Isolated User Meditations"

    # TO STRING METHOD
    def __str__(self):
        return "Isolated User's Meditation " + str(self.user.first_name) + str(self.user.role) + " - " + self.name





#  --- USER PERSONALIZED UPLIFTING CONTENT ---
class FrontlineUpliftingContent(models.Model):

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="frontline_uplifting_content", blank=True)

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
        return "Frontline User's Uplifting Content " + str(self.user.first_name) + str(self.user.role) + " - " + self.title


class UnemployedUpliftingContent(models.Model):

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="unemployed_uplifting_content", blank=True)

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
        return "Unemployed User's Uplifting Content " + str(self.user.first_name) + str(self.user.role) + " - " + self.title


class SurvivorUpliftingContent(models.Model):

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="survivor_uplifting_content", blank=True)

    # DATABASE FIELDS
    title = models.CharField(max_length=200, verbose_name="Article Name")
    description = models.CharField(max_length=200, verbose_name="Article Description")
    img_url = models.URLField(max_length=500, verbose_name="Image URL")
    src = models.CharField(max_length=200, verbose_name="Article Source")
    article_link = models.URLField(max_length=500, verbose_name="Article URL")

    # META
    class Meta:
        verbose_name = "Survivor's Uplifting Content"
        verbose_name_plural = "Survivor Uplifting Content"

    # TO STRING METHOD
    def __str__(self):
        return "Survivor's Uplifting Content " + str(self.user.first_name) + str(self.user.role) + " - " + self.title


class LossUpliftingContent(models.Model):

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="loss_uplifting_content", blank=True)

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
        return "Loss User's Uplifting Content " + str(self.user.first_name) + str(self.user.role) + " - " + self.title


class MentalHealthUpliftingContent(models.Model):

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mentalhealth_uplifting_content", blank=True)

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
        return "Mental Health's Uplifting Content " + str(self.user.first_name) + str(self.user.role) + " - " + self.title



class IsolatedUpliftingContent(models.Model):

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="isolated_uplifting_content", blank=True)

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
        return "Isolated User's Uplifting Content " + str(self.user.first_name) + str(self.user.role) + " - " + self.title