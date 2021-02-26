from django import forms
from django.contrib.auth.forms import UserChangeForm,         UserCreationForm 
from .models import User
 
class AbstractUserCreationForm(UserCreationForm):    
    class Meta:        
        model = User       
        fields = ('email', 'last_login', 'date_joined', 'is_staff')
class AbstractUserChangeForm(UserChangeForm):    
    class Meta:        
        model = User      
        fields = UserChangeForm.Meta.fields