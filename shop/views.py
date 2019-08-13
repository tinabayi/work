from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.

def welcome(request):
    return render(request, 'all-shop/welcome.html')
def home(request):
    store = Store.get_all_store()  

    return render(request, 'index.html',{'store':store})    