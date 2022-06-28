from django import forms 
from user.models import  Products,ProductImage
from django.forms import modelform_factory
class ProductForm(forms.ModelForm):
    """ form to create products"""
    more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        "class": "form-control",
        "multiple": True
    }))
    class Meta:
        model = Products
        fields = ["title", "itemno", "descriptions", "image"]

class ProductEditForms(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

class ImagesForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image',]