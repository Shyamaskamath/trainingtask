from django import forms 
from user.models import  Products,ProductImage
class ProductForm(forms.ModelForm):
    """ form to create products"""
    more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        "class": "form-control",
        "multiple": True
    }))
    class Meta:
        model = Products
        fields = ["title", "itemno", "descriptions", "image"]
