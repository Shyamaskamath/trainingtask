from re import I
from django import http
from django.http import Http404, HttpResponseRedirect
from django.views import generic
from .forms import InviteUserForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm

class RegisterationFormView(LoginRequiredMixin,generic.CreateView):
    """ view for user registeration """
    template_name = 'user/register.html'
    form_class = InviteUserForm
    success_message = "user was created successfully"
    success_url = reverse_lazy("home")

class LoginView(FormView):
    """view for user login"""
    form_class = AuthenticationForm
    template_name = "user/login.html"
    success_url = reverse_lazy("home")
    
    def form_valid(self,form):
        """Override method"""
        login(self.request,form.get_user())
        return HttpResponseRedirect(self.get_success_url())




   