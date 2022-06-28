from django.urls import path
from .import views

urlpatterns = [
    path('',views.LoginView.as_view(),name="login"),
    path('register/',views.RegisterationFormView.as_view(),name="createuser"), 
] 