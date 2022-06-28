from django.contrib import admin
# Register your models here.
from .models import CustomUser,ProductImage,Products

@admin .register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """ registering and creating view to dispaly  table in admin """
    list_display = ['email','roles','is_staff','is_admin','is_superuser']



class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

    class Meta:
       model = Products
       

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass