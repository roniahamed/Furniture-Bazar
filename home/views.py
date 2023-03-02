from itertools import product
from django.shortcuts import render
from products.models import *
from .models import *
# Create your views here.

def home_page(request):
    
    slider = Slide.objects.all()[:5]
    feature =Products.objects.filter(category_id=2)
    products1 =Products.objects.all().order_by('-date_added')[:8]
    
    context = {
        'slider':slider,
        'features':feature,
        'products1':products1,
       
    }
    
    return render(request,'./home/home.html',context)


