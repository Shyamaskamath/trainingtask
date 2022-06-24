from django.contrib import admin
# Register your models here.
from .models import CustomUser,Products,ProductImage

@admin .register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email','roles','is_staff','is_admin','is_superuser']


@admin .register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','itemno','descriptions']

@admin .register(ProductImage)
class ProductImage(admin.ModelAdmin):
    list_display = ['id']