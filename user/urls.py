from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

urlpatterns = [
   
    path('register',views.register,name="signup"),
    path('home/',views.home,name="home"),
    path('login_request/',views.login_request,name="login"),
  

]