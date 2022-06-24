from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.HomePageView.as_view(),name="home"),
    path('register',views.RegisterationFormView.as_view(),name="createuser"), 
    path('logout/',auth_views.LogoutView.as_view(next_page="login"), name='logout'), 
] 