from django.contrib import admin
# Register your models here.
from .models import CustomUser,ProductImage,Products

@admin .register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """ registering and creating view to dispaly  table in admin """
    list_display = ['email','roles','is_staff','is_admin','is_superuser',]


@admin .register(Products)
class ProductAdmin(admin.ModelAdmin):
    """ registering and creating view to dispaly  table in admin """
    list_display = ['title','itemno','descriptions','image']

@admin .register(ProductImage)
class ProductImage(admin.ModelAdmin):
    """ registering and creating view to dispaly  table in admin """
    list_display = ['id']  


