

from django.shortcuts import render, redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login
from django.contrib import messages


@login_required(login_url='login')
def home(request):
    return render(request,'user/home.html')

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form = RegistrationForm()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'user/register.html',{'form':form})

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

    form = LoginForm()
    return render(request = request,
                    template_name = "user/login.html",
                    context={"form":form})