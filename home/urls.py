from django.contrib import admin
from django.urls import path
from home import views #we are importing the view file

urlpatterns = [
    path("",views.index, name='home'), #if anyone comes in the path (http://127.0.0.1:8000/) go to index page in the view
    path("about",views.about, name='about'), #if anyone comes in (http://127.0.0.1:8000/about) go to the about page
    path("service",views.service,name='service'),
    path("contact",views.contact,name='contact')

 
]