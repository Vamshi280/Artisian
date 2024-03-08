from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.utils import timezone



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


    #product and catiogray table

class Category(models.Model):
      name = models.CharField(max_length=100, unique=True)

      def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    manufacturer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product) #many to many relationship between product and cart products
    created_at = models.DateTimeField(auto_now_add=True)

    def add_to_cart(self, product):
        self.products.add(product)

    def remove_from_cart(self, product):
        self.products.remove(product)

    def clear_cart(self):
        self.products.clear()
    def calculate_total_price(self):
        total_price = sum(product.price for product in self.products.all())
        return total_price




#order table
class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField(null=True) 

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"