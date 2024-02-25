from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)



class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    # Add other fields for customer details as needed

class Artisan(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    # Add other fields for artisan details as needed
