from django.contrib import admin
# Register your models here.
from .models import CustomUser

@admin .register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """ registering and creating view to dispaly  table in admin """
    list_display = ['email','roles','is_staff','is_admin','is_superuser']



