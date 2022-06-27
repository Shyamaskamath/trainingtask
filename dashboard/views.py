from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import redirect_to_login
from user.models import CustomUser, Products,ProductImage
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

class ProductListView(LoginRequiredMixin,ListView):
    """ view for list all product dashboard page"""
    model = Products
    context_object_name = "products" 
    template_name = "dashboard/productlist.html"
   
class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Products
    context_object_name = "products"
    template_name = "dashboard/productdetail.html" 
    
class AddProductView(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    """ view for adding new products """
    model = Products
    form_class = ProductForm
    template_name = "dashboard/addproduct.html"
    success_url = reverse_lazy('home')
    permission_required = 'dashboard.add_products'
    def form_valid(self, form):
        p = form.save()
        images = self.request.FILES.getlist("more_images")
        for i in images:
            ProductImage.objects.create(products=p, image=i)
        return super().form_valid(form)

    
class ProductUpdateView(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    """  view for updating the product details"""
    model = Products
    form_class = ProductForm
    template_name = "dashboard/productupdate.html"
    success_url = reverse_lazy('home')
    permission_required = 'dashboard.change_products'
    

class ProductDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    """ view to delete the products """
    model = Products
    context_object_name = 'products'
    template_name = "dashboard/deleteproduct.html"
    success_url = reverse_lazy('home')
    permission_required = 'dashboard.delete_products'

