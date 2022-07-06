from django.urls import path
from . views import  RegistrationAPIView,LoginAPIView
from . import views

urlpatterns = [
    path('register/',RegistrationAPIView.as_view()),
    path('login/',LoginAPIView.as_view()),
    path('product/',views.ProductListAPIView.as_view()),
    path('product/<int:pk>/',views.ProductDetailAPIView.as_view()),
    path('product/<int:pk>/edit/',views.ProductUpdateAPIView.as_view()),
    path('product/<int:pk>/delete/',views.ProductDeleteAPIView.as_view()),
    path('product/create/',views.CreateViewset.as_view( {"post": "create"})),
]