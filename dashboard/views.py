from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import NewUserCreationForm
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth import views as auth_view, REDIRECT_FIELD_NAME, logout
from django.urls import path
# Create your views here.

class StaffRequiredMixin(AccessMixin):
    """Verify that the current user is admin """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.add_message(request, level=messages.ERROR,
                                 message="Please login as Admin to see the  page.")
            logout(request)
            return redirect_to_login(
                path,
                login_url=reverse_lazy('login'),
                redirect_field_name=REDIRECT_FIELD_NAME,
            )
        return super().dispatch(request, *args, **kwargs)


class HomePageView(StaffRequiredMixin,LoginRequiredMixin,TemplateView):
    """view for home page"""
    template_name = "dashboard/homepage.html"


class RegisterationFormView(StaffRequiredMixin,LoginRequiredMixin,generic.CreateView):
    """ view for user creation  """
    template_name = 'dashboard/usercreation.html'
    form_class =NewUserCreationForm
    success_url = reverse_lazy("home")
    
    