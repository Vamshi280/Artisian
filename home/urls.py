from django.contrib import admin
from django.urls import path
from home import views #we are importing the view file
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index, name='home'), #if anyone comes in the path (http://127.0.0.1:8000/) go to index page in the view
    path("about",views.about, name='about'), #if anyone comes in (http://127.0.0.1:8000/about) go to the about page
    path("service",views.service,name='service'),
    path("contact",views.contact,name='contact'),
    path("register",views.register,name='register'),
    path("login",views.login,name='login'),
    path('check_username/', views.check_username, name='check_username'),
    path('logout', views.logout, name='logout'),
    path('product/<int:product_id>', views.view_product, name='view_product'),





 
]