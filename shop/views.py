from django.shortcuts import render
from django.http  import HttpResponse
from .models import Product,Image
# Create your views here.

def welcome(request):

    products =Product.get_product()
    return render(request, 'all-shop/welcome.html', {"products":products})

def product(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-shop/home.html", {"image":image})