from django import forms
from .models import Product,ProductImage

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