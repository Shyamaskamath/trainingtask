from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.UserRegistrationAPI.as_view()),
    path('login/',views.LoginAPI.as_view()),
    path('product/',views.ProductListAPI.as_view()),
    path('product/<int:pk>/',views.DetailProductListAPI.as_view()),
    path('product/<int:pk>/edit/',views.ProductUpdateAPI.as_view()),
    path('product/<int:pk>/delete/',views.DeleteProductAPI.as_view()),
    path('product/create/',views.ProductCreateAPI.as_view( {"post": "create"})),
    path('profileupdate/<int:pk>/',views.ProfileUpdateAPI.as_view(),name="profileupdate"),
]