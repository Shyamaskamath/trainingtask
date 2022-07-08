import email
from pyexpat import model
from django import forms
from user.models import CustomUser 
from .models import Product,ProductImage
from django.forms import modelformset_factory
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    """form to create new products"""
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageForm(forms.ModelForm):
    """form to add product images"""
    
    class Meta:
        model = ProductImage
        fields = ('image',)

class ProductEditForm(forms.ModelForm):
    """form to edit product detais"""
    class Meta:
        model = Product
        fields = '__all__'

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','mobile','profile_photo')

"""formset  to get 3 image per product """
ImageFormSet = modelformset_factory(ProductImage, form=ProductImageForm, extra=3,max_num=3,min_num=0)