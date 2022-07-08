from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from .roles import *


class CustomUserManager(BaseUserManager):
    """custom manager for custom usermodel  """
    def create_user(self, email, username, password=None):
        user = self.model( email=self.normalize_email(email),
            username=str(email).lower())
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
    first_name = models.CharField(max_length=10,null=True,blank=True, default='')
    last_name = models.CharField(max_length=15,null=True,blank=True, default='')
    mobile = models.CharField(max_length=20, blank=True, default='') 
    profile_photo = models.FileField(verbose_name="Profilepic",upload_to="profile/",max_length=255,
                              null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
   



