from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.HomePageView.as_view(),name="dashboardhome"),
    path('register',views.RegisterationFormView.as_view(),name="createuser")
   
] 