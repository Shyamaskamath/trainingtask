from telnetlib import Telnet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from .forms import UserRegistrationForm,LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


''' function based view for rendering  homepage  '''

@login_required(login_url='login')
def homepageview(request):
    return render(request,'user/home.html')


''' Class  based view for rendering  homepage  '''
class HomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'user/home.html'

'''class bassed view for  new user creation/registration'''

class RegisterationFormView(generic.CreateView):
    template_name = 'user/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")

'''Function based view for new user creation/registration '''

def registerformview(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserRegistrationForm()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,'user/register.html',{'form':form})

'''function based view to implement Login'''

# def loginformview(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')

#     form = LoginForm()
#     return render(request = request,
#                     template_name = "user/login.html", context={"form":form})

'''class based view  to implement login '''
class LoginFormView(generic.View):
    template_name = 'user/login.html'
    form_class = LoginForm

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{"form":form})

    
    def post(self,request):
            form = self.form_class(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
            message = "Login Failed invalid username or password!"
            return render(request,self.template_name,{"form":form,"message":message})

''' class based view for ogin using Formview'''
class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "user/login.html"
    success_url = reverse_lazy("home")
 
    def form_valid(self,form):
        # print(form.get_user())
        # print(self.request.POST['username'])
        login(self.request,form.get_user())
        return HttpResponseRedirect(self.get_success_url())




   