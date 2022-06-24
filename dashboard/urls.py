from django.urls import path
from .import views
urlpatterns = [
    path('',views.HomePageView.as_view(),name="home"),
    path('register',views.RegisterationFormView.as_view(),name="createuser"), 
    path('product/',views.ProductListView.as_view(),name="productlist"),
    path('product/<int:pk>/',views.ProductDetailView.as_view(),name="productdetails"),
    path('product/<int:pk>/delete/',views.ProductDeleteView.as_view(),name="deleteproduct"),
    # path('product/create/',views.AddProductView.as_view(),name="addproduct"),
    # path('product/<int:pk>/edit/',views.ProductUpdateView.as_view(),name="updateproduct"),
] 