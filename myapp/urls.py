from django.urls import path
from .import views
urlpatterns = [
    path('',views.HomePageView.as_view(),name="homepage"),
    path('people/',views.PeoplePageView.as_view(),name="people"),
    path('product/create/',views.AddProductView.as_view(), name="addproduct"),
    path('product/<int:pk>/',views.DetailProductView.as_view(),name="details"),
    path('product/<int:pk>/edit/',views.ProductEditView.as_view(),name="editproduct"),
    path('product/',views.ProductListView.as_view(),name="productlist"),
    path('product/<int:pk>/delete/',views.DeleteProductView.as_view(),name="deleteproduct"),
    path('profileupdate/<int:pk>/',views.ProfileUpdateView.as_view(),name="profileupdate"),
]