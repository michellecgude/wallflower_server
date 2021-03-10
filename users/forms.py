from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User # UserProfile

# Allows make/modify users from the admin application & within the project itself

class AbstractUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        # fields = ('username', 'email')

        fields = ('username', 'email', 'password', "role")


class AbstractUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields