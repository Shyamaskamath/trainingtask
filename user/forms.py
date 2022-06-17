from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
''' cform for new user creation '''
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
''' Form for user login '''
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget= forms.PasswordInput)

