import django
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   
    path('register/',views.Register.as_view(),name="signup"),
    path('home/',views.HomePage.as_view(),name="home"),
    path('login_request/',views.login_request.as_view(),name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page="login"), name='logout'),
   
  

]