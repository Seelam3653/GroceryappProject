from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from . forms import CustomUserCreationForm,LoginForm
from .models import Product, Order, Cart, CartItem


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def user_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request,'signup.html',{'form':form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user:
                login(request, user)
                return redirect('home')                           
    else:
        form = LoginForm()    
    return render(request, 'login.html',{'form': form})

  
def user_logout(request):
    logout(request)
    return redirect('home')

def placeOrder(request):
    return render(request, 'myorders.html')
 

def mycart(request):
    return render(request,'mycart.html')


