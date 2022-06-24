from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model   
from django.core.exceptions import ValidationError
from user.roles import *

def validatemail(value):
    """checking if given email alreday taken """
    User = get_user_model() 
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value} is taken!"),params = {'value':value})

class NewUserCreationForm(UserCreationForm):
    """User Creation form """
    email = forms.EmailField(validators = [validatemail])
    roles = forms.ChoiceField(choices=roles)
    password1 = forms.CharField(widget = forms.HiddenInput(), required = False)
    password2 = forms.CharField(widget = forms.HiddenInput(), required = False)
    class Meta:
        model = get_user_model() 
        fields = ['email']
        
