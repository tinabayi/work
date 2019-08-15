from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .models import Product,Image, Cart

# Create your views here.

def welcome(request):

    products =Product.get_product()
    return render(request, 'all-shop/welcome.html', {"products":products})

def product_func(request,product_id):
    try:
        image = Product.objects.get(id =product_id)
        
    except DoesNotExist:
        raise Http404()
    return render(request,"all-shop/home.html", {"image":image})

def add_cart(request,product_id):
    one_product=Product.objects.filter(id=product_id).first()
    cart=Cart(products=one_product,user=request.user)  
    cart.save()
    return redirect('/display')

def display_cart(request):
    
    cart= Cart.objects.filter(user=request.user).all()
    for item in cart:
        print(item.products)
    return render(request,"all-shop/cart.html", {"cart":cart})
