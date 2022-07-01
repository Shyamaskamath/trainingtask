from django.shortcuts import redirect, render
from .forms import ProductForm, ProductImageForm, ProductEditForm,ImageFormSet
from .models import ProductImage, Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView,FormView,UpdateView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin,AccessMixin
from django.views.generic import TemplateView, CreateView
from user.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.contrib import messages
from django.views import View
# Create your views here.

class StaffRequiredMixin(AccessMixin):
    """
    View mixin which checks user is a staff member"""
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(
                request,
                'You do not have the permission required to perform the '
                'requested operation.')
            return redirect(settings.LOGIN_URL)
        return super(StaffRequiredMixin, self).dispatch(request,
            *args, **kwargs)

class HomePageView(LoginRequiredMixin, TemplateView):
    """ view for homepage"""
    template_name = 'myapp/homepage.html'


class PeoplePageView(LoginRequiredMixin,StaffRequiredMixin,ListView):
    """views for getting list adminusers and customerusers """
    template_name = "myapp/people.html"
    model = CustomUser
    def get_context_data(self, **kwargs):
        objectlist = super(PeoplePageView, self).get_context_data(**kwargs)
        objectlist['admin'] = CustomUser.objects.filter(groups__name='adminusers')
        objectlist['customer'] = CustomUser.objects.filter(groups__name='customer')
        return objectlist

class ProductListView(LoginRequiredMixin, ListView):
    pass
    """ view for rendering all the products """
    model = Product
    context_object_name = 'product'
    template_name = 'myapp/productlist.html'

class DeleteProductView(LoginRequiredMixin,StaffRequiredMixin, DeleteView):
    """view to delete a product"""
    model = Product
    context_object_name = "product"
    template_name = "myapp/deleteproduct.html"
    success_url = reverse_lazy('productlist')
    
class DetailProductView(LoginRequiredMixin, DetailView):
    """ view for displaying detailed view of a product"""
    context_object_name = "product"
    model = Product
    template_name = "myapp/detail.html"

class AddProductView(LoginRequiredMixin,StaffRequiredMixin,CreateView):
    """view to create new product"""
    model = Product
    template_name = 'myapp/productcreate.html'
    form_class = ProductForm
    object = None

    def get(self, request, *args, **kwargs):
        productform = ProductForm()
        formset = ImageFormSet(queryset=ProductImage.objects.none())
        return render(request, 'myapp/productcreate.html', {"productform": productform, "formset": formset})
    
    def post(self, request, *args, **kwargs): 
        productform = ProductForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)
        if productform.is_valid() and formset.is_valid():
            p = productform.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    ProductImage.objects.create(image=image, product=p)
            return redirect("productlist")
        else:
            print(productform.errors, formset.errors)   

class ProductEditView(LoginRequiredMixin,StaffRequiredMixin,UpdateView):
    """view to update product details"""
    template_name = "myapp/edit.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('productlist')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object.id)
        form = ProductEditForm(instance=self.object)
        formset =  ImageFormSet(queryset=ProductImage.objects.filter(product= self.object))
        context = {
            'form': form,
            'formset':formset,
        }
        
        return render(request,'myapp/edit.html',context)

    def post(self, request, *args, **kwargs): 
        product = self.get_object()
        form = ProductEditForm(request.POST,instance=product)
        formset =  ImageFormSet(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            form.save() 
            for image in formset.forms:
                if image.is_valid():
                    if image.cleaned_data.get('image'):
                        image.instance.product = product
                        image.instance.save()
                        image.save()   
        return HttpResponseRedirect(product.get_absolute_url()) 
            