from django.shortcuts import redirect, render, HttpResponse
from .models import User,Customer, Artisan
from django.contrib.auth.hashers import make_password


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




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        phone_number = request.POST.get('phone_number', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        pincode = request.POST.get('pincode', '')

        #making hased password
        hashed_password = make_password(password)
        print(hashed_password)

        # Check if username already exists
        if Customer.objects.filter(username=username).exists() or Artisan.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists.'})

        # Create a new user object based on user type
        if user_type == 'customer':
            customer = Customer(username=username, password=hashed_password, first_name=first_name,
                                last_name=last_name, email=email, phone_number=phone_number,
                                address=address, pincode=pincode)
            customer.save()
        else:
            artisan = Artisan(username=username, password=hashed_password, first_name=first_name,
                              last_name=last_name, email=email, phone_number=phone_number,
                              address=address, pincode=pincode)
            artisan.save()

        return redirect('login')  # Redirect to login page after successful registration

    return render(request, 'signup.html')


def login(request):
    return render(request,"signin.html")

from django.http import JsonResponse
from .models import Customer, Artisan

#for checking whether the username exists in database
def check_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        # Check if the username exists in the Customer or Artisan table
        customer_exists = Customer.objects.filter(username=username).exists()
        artisan_exists = Artisan.objects.filter(username=username).exists()

        return JsonResponse({'exists': customer_exists or artisan_exists})

    # Return an empty response if the request method is not POST
    return JsonResponse({})


