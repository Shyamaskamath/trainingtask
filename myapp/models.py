from django.db import models
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    """ model to store product detail """
    title = models.CharField(max_length=100)
    itemno= models.CharField(max_length=20,unique=True)
    description = models.TextField()

    @property
    def  ProductImage(self):
        return self.ProductImage_set.all()

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})


class ProductImage(models.Model):
    """model to store multiple images of a product """
    product = models.ForeignKey(Product,on_delete= models.CASCADE, related_name="images")
    image = models.ImageField(upload_to= product,null=True,blank =True )
    
    def get_absolute_url(self):
        return reverse('productlist')
