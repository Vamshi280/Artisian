"""
URL configuration for basic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#To change the admin text
admin.site.site_header = "vamshi is the Admin"
admin.site.site_title = "vamshi admin Portal"
admin.site.index_title = "Welcome to vamshi Researcher Portal"

urlpatterns = [
    #whem we start server if we give port number along /admin it will tale to admin page
    path('admin/', admin.site.urls),
    #other the admin page any other path forward to
    path('',include("home.urls")) #home is the app name and urls is the file name in the app
]
