from django.contrib import admin
from .models import Product,ProductImage
# Register your models here.


class ProductImageInline(admin.TabularInline):
    """ creating a tabular view """
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]