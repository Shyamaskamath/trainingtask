from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validateemail(value):
    """checking if given email alreday taken or not"""
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value} is taken!"),params = {'value':value})

class UserCreationForm(UserCreationForm):
    """Registartion  form"""
    email = forms.EmailField(validators = [validateemail])
    is_staff = forms.BooleanField(required=False)

    class Meta:
        """overridig the meta class"""
        model = User
        fields = ['username','email','password1','password2','is_staff']
        
