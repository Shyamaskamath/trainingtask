from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from user.roles import *
from .models import CustomUser
from django.contrib.auth.models import Group

def validatemail(value):
    """checking if given email alreday taken """
    User = get_user_model() 
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value} is taken!"),params = {'value':value})

class InviteUserForm(UserCreationForm):
    """User Creation form  """
    email = forms.EmailField(validators = [validatemail])
    groups = forms.ModelMultipleChoiceField(queryset= Group.objects.all(),widget = forms.CheckboxSelectMultiple())
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password1 = forms.CharField(widget = forms.HiddenInput(), required = False)
    password2 = forms.CharField(widget = forms.HiddenInput(), required = False)
    class Meta:
        model = CustomUser
        fields = ['email','groups']

    def save(self,commit=True):
        user = CustomUser.objects.create(
            email = self.cleaned_data.get('email'),
        )
        
        user.set_password(self.cleaned_data.get('password'))
        user.groups.add(self.cleaned_data.get('groups')[0].id)
        print(self.cleaned_data)
        user.save()
        return user

    

    
