from django.shortcuts import render, redirect
from django.views import generic
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth



# @login_required(login_url='login')
# def home(request):
#     return render(request,'user/home.html')

class HomePage(LoginRequiredMixin,TemplateView):
    template_name = 'user/home.html'


class Register(generic.CreateView):
    template_name = 'user/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy("login")


# def register(request):
#     if request.method =='POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = RegistrationForm()
#             return redirect('login')
#     else:
#         form = RegistrationForm()
#     return render(request,'user/register.html',{'form':form})

# def login_request(request):
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

class login_request(generic.View):
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



    
            


        
        



   



