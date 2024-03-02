from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import check_password


from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    # Provide custom related names for groups and user_permissions fields
    class Meta:
        permissions = (("can_add_items", "Can add items"),)  # Define custom permission

    def __str__(self):
        return self.username

class Artisan(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    # Provide custom related names for groups and user_permissions fields
    class Meta:
        permissions = (("can_add_items", "Can add items"),)  # Define custom permission

    def __str__(self):
        return self.username
