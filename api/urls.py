from django.urls import path
from rest_framework.authtoken import views
from . views import RegisterUserAPIView

urlpatterns = [
   
    path('register/',RegisterUserAPIView.as_view()),
    path('api-token-auth/',views.obtain_auth_token ),  
]