from django.shortcuts import render
from products.models import Products
# Create your views here.

def home_page(request):
    
    slider = Products.objects.all()
    context = {
        'slider':slider
    }
    
    return render(request,'./home/home.html',context)
