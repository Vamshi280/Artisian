from django.shortcuts import redirect, render, HttpResponse
from .models import Customer, Artisan ,Product,Cart,Order
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login 
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, get_object_or_404
import random





# Create your views here.
def index(request):
     # Retrieve all products from the database
    products = list(Product.objects.all())
    #to shuffle the product we use random
    random.shuffle(products)
     # Pass the products to the template
    return render(request,'index.html',{'products':products}) #request template page to render sending the parameter to page
    #instead of httpresponse we will render the page
    # return HttpResponse("This is a homepage")
def about(request):
    return render(request,"about.html")
def service(request):
    return render(request,"service.html")
def contact(request):
    return render(request,"contact.html")


def logout(request):
    auth_logout(request)
    return redirect('home')  # Redirect to login page after logout

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

#login page authintication
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST.get('user_type')
        # Authenticate the user based on the selected user type
        user = None
        is_artisan = False  # Default value

        # Authenticate the user based on the selected user type
        if user_type == 'customer':
            user = authenticate_customer(username, password)
        elif user_type == 'artisan':
            user = authenticate_artisan(username, password)
            is_artisan=True
        else:
            # Invalid user type, handle the error as needed
            return render(request, 'signin.html', {'error': 'Invalid user type'})

        # Check if authentication was successful
        if user:
            # Redirect all users to the home page
            auth_login(request,user)
            return redirect('home')  # Replace with actual URL name for your home page
        else:
            # Authentication failed, handle the error as needed
            return render(request, 'signin.html', {'error': 'Invalid username or password'})

    # Render the login page if it's a GET request or if authentication fails
    return render(request, 'signin.html')

def authenticate_customer(username, password):
    try:
        customer = Customer.objects.get(username=username)
        if customer.check_password(password):
            return customer
    except Customer.DoesNotExist:
        pass
    return None

def authenticate_artisan(username, password):
    try:
        artisan = Artisan.objects.get(username=username)
        if artisan.check_password(password):
            return artisan
    except Artisan.DoesNotExist:
        pass
    return None



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


#creating view of product here
def view_product(request, product_id):
    # Retrieve the product from the database
    product = get_object_or_404(Product, pk=product_id)
    
    # Pass the product to the view template
    return render(request, 'view_product.html', {'product': product})


# implementing cart
def view_cart(request):
    # Retrieve the user's cart
    cart = Cart.objects.filter(user=request.user).first()
    return render(request, 'cart.html', {'cart': cart})

#when user is not logged in if he press login button it will redirect to login page
@login_required
def add_to_cart(request, product_id):
    # Retrieve the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)
    # Add the product to the cart
    cart.products.add(product_id)
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    # Retrieve the user's cart
    cart = Cart.objects.filter(user=request.user).first()
    # Remove the product from the cart
    cart.products.remove(product_id)
    return redirect('view_cart')


@login_required
def place_order(request):
    if request.method == 'POST':
        # Retrieve the user's cart
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            # Process the order and save it to the database
            # Create the order
            order = Order.objects.create(
                user=request.user,
                total_price=cart.calculate_total_price(),
                address=request.user.address
            )
            # Add products from cart to the order
            order.products.add(*cart.products.all())
            # Clear the cart
            cart.clear_cart()
            # Redirect to the order confirmation page
            return redirect('order_confirmation', order_id=order.id)
    else:
        # Display the order page with cart items
        cart = Cart.objects.filter(user=request.user).first()
        return render(request, 'order.html', {'cart': cart})

@login_required
def order_from_home(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'order.html', {'product': product})

def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    # Fetch products with price information
    products = order.products.all()
    # Calculate the total price based on individual product prices
    total_price = sum(product.price for product in products)
    return render(request, 'order_confirmation.html', {'order': order, 'total_price': total_price})









