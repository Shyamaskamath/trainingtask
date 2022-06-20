from django.http import HttpResponseRedirect
from django.views import generic
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect


class AdminHomePageView(TemplateView):
    """view for home page for adminstaff """
    template_name = 'user/adminhome.html'

    @method_decorator(staff_member_required,login_required)
    def dispatch(self,  *args, **kwargs): 
        return super().dispatch( *args, **kwargs)


class RegisterationFormView(generic.CreateView):
    """ view for user registeration """
    template_name = 'user/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    @method_decorator(staff_member_required)
    def dispatch(self,  *args, **kwargs): 
        return super().dispatch( *args, **kwargs)
    
class LoginView(FormView):
    """view for user login"""
    form_class = AuthenticationForm
    template_name = "user/login.html"
    success_url = reverse_lazy("home")
    
    def form_valid(self,form):
        """Override method"""
        login(self.request,form.get_user())
        return HttpResponseRedirect(self.get_success_url())




   