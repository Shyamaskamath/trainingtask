from django.urls import path
from .import views
urlpatterns = [
    path('',views.HomePageView.as_view(),name="homepage"),
    path('people/',views.peoplepageview,name="people"),
    path('product/create/',views.createview, name="addproduct"),
    path('product/<int:pk>/',views.DetailProductView.as_view(),name="details"),
    path('product/<int:pk>/edit/',views.editview,name="editproduct"),
    path('product/',views.ProductListView.as_view(),name="productlist"),
    path('product/<int:pk>/delete/',views.DeleteProductView.as_view(),name="deleteproduct"),
]