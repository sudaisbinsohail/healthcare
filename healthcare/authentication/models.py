from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255 , blank=True)
    date_of_birth = models.DateField(null=True , blank=True)
    gender = models.CharField(max_length=255, null=True , blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True , blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2 , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


