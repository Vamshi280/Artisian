from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import check_password


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)



class Artisan(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

