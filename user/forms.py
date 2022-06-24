from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model  
User = get_user_model()  
from django.core.exceptions import ValidationError
roles = [
  ('admin','admin'),
  ('staff','staff')
]
def validateemail(value):
    """checking if given email alreday taken """
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value} is taken!"),params = {'value':value})

class NewUserCreationForm(UserCreationForm):
    """User Creation form"""
    email = forms.EmailField(validators = [validateemail])
    roles = forms.ChoiceField(choices=roles)
    password1 = forms.CharField(widget = forms.HiddenInput(), required = False)
    password2 = forms.CharField(widget = forms.HiddenInput(), required = False)
    class Meta:
        model = User
        fields = ['email']
        
