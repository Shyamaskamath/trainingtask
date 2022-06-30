from pipes import Template
from django.shortcuts import redirect, render
from .forms import ProductForm, ProductImageForm, ProductEditForm
from .models import ProductImage, Product
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin,AccessMixin
from django.views.generic import TemplateView, CreateView
from user.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.contrib import messages
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

@login_required(login_url='login')
@staff_member_required(login_url='login')
def peoplepageview(request):
    """ view to render the number of custeomers and admins in created in the site"""
    customer = CustomUser.objects.filter(groups__name='customer')
    admin = CustomUser.objects.filter(groups__name='adminusers')
    context = {
            'admin': admin,
            'customer': customer,
        }
    return render(request,"myapp/people.html",context)

        


class ProductListView(LoginRequiredMixin, ListView):
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


@login_required(login_url='login')
@staff_member_required(login_url='login')
def createview(request):
    """ view for creating a new product"""
    ImageFormSet = modelformset_factory(
        ProductImage, form=ProductImageForm, extra=4)
    if request.method == "GET":
        productform = ProductForm()
        formset = ImageFormSet(queryset=ProductImage.objects.none())
        return render(request, 'myapp/productcreate.html', {"productform": productform, "formset": formset})
    elif request.method == "POST":
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

@login_required(login_url='login')
@staff_member_required(login_url='login')
def editview(request,pk):
    product = get_object_or_404(Product,pk=pk)
    
    imageFormSet = modelformset_factory(ProductImage,fields=('image',),extra=4,max_num=4)
    if request.method == 'POST':
        form = ProductEditForm(request.POST,instance=product)
        formset = imageFormSet(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            form.save()
            # print(formset.cleaned_data)
            existing_images = ProductImage.objects.filter(product=product)
            print(existing_images)
            for index,f in enumerate(formset):
                if f.cleaned_data:
                    if f.cleaned_data['id'] is None:
                        product = ProductImage(product=product,image=f.cleaned_data['image'])
                        product.save()
                    elif f.cleaned_data['image'] is False:
                        photo = ProductImage.objects.get(id=request.POST.get('form-'+str(index)+'-id'))
                        photo.delete()
                    else:
                        photo = ProductImage(product=product,image=f.cleaned_data['image'])
                        data = ProductImage.objects.get(id=existing_images[index].id)
                        data.image = photo.image
                        data.save()
        return HttpResponseRedirect(product.get_absolute_url())
                           
    form = ProductEditForm(instance=product)
    formset = imageFormSet(queryset=ProductImage.objects.filter(product=product))
    context = {
        'form': form,
        'formset':formset,
        'product':product
        
    }
    
    return render(request,'myapp/edit.html',context)
    