from django.db import models
from users.models import User
from django.conf import settings

# --- USER JOURNALS ---
class Journal(models.Model):

    # RELATIONSHIP
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_journals")

    # DATABASE FIELDS
    title = models.CharField(max_length=200, verbose_name="Journal Title")
    body = models.TextField(max_length=3000, verbose_name="Journal Body")
    date_created = models.DateField(auto_now_add=True, verbose_name="Journal Date Created")

    # META
    class Meta:
        verbose_name = "User Journal Entry"
        verbose_name_plural = "User Journal Entries"

    # TO STRING METHOD
    def __str__(self):
        return str(self.journal_title) + " written by " + str(self.user.first_name)