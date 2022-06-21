from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    is_admin  = models.BooleanField('is_admin',default=False)
    is_user  = models.BooleanField('is_user',default=False)


