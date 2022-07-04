from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from user.roles import *
from .models import CustomUser
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from django.core import validators

def validatemail(value):
    """checking if given email alreday taken """
    User = get_user_model() 
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value} is taken!"),params = {'value':value})

class InviteUserForm(UserCreationForm):
    """User Creation form  """
    email = forms.EmailField(validators = [validatemail])
    username  = forms.CharField(widget = forms.HiddenInput(), required = False)
    roles = forms.ModelMultipleChoiceField(queryset= Group.objects.all(),widget = forms.CheckboxSelectMultiple())
    password=forms.CharField(widget=forms.PasswordInput,validators=[validate_password])
    password1 = forms.CharField(widget = forms.HiddenInput(), required = False)
    password2 = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        model = CustomUser
        fields = ['email']

    def save(self,commit=True):
        user = CustomUser.objects.create(
            email = self.cleaned_data.get('email'),
            username = str(self.cleaned_data.get('email')).lower()

        )
        user.set_password(self.cleaned_data.get('password'))
        my_group = mygroup = ""
        if (self.cleaned_data.get('roles')[0].id) == 3:
            my_group = Group.objects.get(name='adminusers') 
            my_group.user_set.add(user)
            user.is_staff = True
            user.is_admin = True
        else:
            mygroup = Group.objects.get(name='customer') 
            mygroup.user_set.add(user)
        user.save()
        return user


    
