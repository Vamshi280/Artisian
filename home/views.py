from django.shortcuts import render, HttpResponse
from .models import User

# Create your views here.
def index(request):
    context={
        'variable':'vamshi'
    }
    return render(request,'index.html',context) #request template page to render sending the parameter to page
    #instead of httpresponse we will render the page
    # return HttpResponse("This is a homepage")
def about(request):
    return render(request,"about.html")
def service(request):
    return render(request,"service.html")
def contact(request):
    if request.method =="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        User.objects.create(email=email,password=password)
        return render(request, "index.html")
    return render(request,"contact.html")
