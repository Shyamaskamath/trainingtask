from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    """Registartion  form"""
    email = forms.EmailField()
    class Meta:
        """configuring  registartion form"""
        model = User
        fields = ['username','email','password1','password2']
        

