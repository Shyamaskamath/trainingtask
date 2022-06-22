from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validateemail(value):
    """checking if given email alreday taken """
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value} is taken!"),params = {'value':value})

class NewUserCReationForm(UserCreationForm):
    """User Creation form"""
    email = forms.EmailField(validators = [validateemail])
    is_staff = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username','email','password1','password2','is_staff']
        
