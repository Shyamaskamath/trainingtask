from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from .roles import *

class CustomUserManager(BaseUserManager):
    """custom manager for custom usermodel  """
    def create_user(self, email, username, password=None):
        user = self.model( email=self.normalize_email(email),
            username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser,PermissionsMixin):
    """ custom usermodel  """
    objects = CustomUserManager()

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    roles = models.CharField(max_length=10,choices=roles,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Products(models.Model):
    """ model for the product """
    title = models.CharField(max_length=20)
    itemno = models.CharField(max_length=8,unique=True)
    descriptions = models.TextField()
    image = models.ImageField(blank =True)

class ProductImage(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")



