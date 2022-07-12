from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.UserRegistrationAPI.as_view()),
    path('login/',views.LoginAPI.as_view()),
    path('product/',views.ProductListAPI.as_view()),
    path('product/<int:pk>/',views.DetailProductListAPI.as_view()),
    path('product/<int:pk>/modify/',views.RetriveUpdateDeleteProductAPI.as_view()),
    path('product/listcreate/',views.ProductListCreateAPI.as_view( {"post": "create","get":"list"})),
    path('profileupdate/<int:pk>/',views.ProfileUpdateAPI.as_view(),name="profileupdate"),
]