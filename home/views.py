from itertools import product
from django.shortcuts import render
from products.models import *
from .models import *
# Create your views here.

def home_page(request):
    
    slider = Slide.objects.all()[:5]
    feature1 =Products.objects.filter(category_id=1).order_by('-date_added')[:1]
    feature2 =Products.objects.filter(category_id=5).order_by('-date_added')[:1]
    feature3 =Products.objects.filter(category_id=8).order_by('-date_added')[:1]
    feature4 =Products.objects.filter(category_id=4).order_by('-date_added')[:1]
    products1 =Products.objects.all().order_by('-date_added')[:8]
    products2 =Products.objects.all().order_by('quantity')[:8]
    offer_product = Products.objects.filter(discount__gte=2).order_by('-discount')[:1]


    
    context = {
        'slider':slider,
        'features1':feature1,
        'features2':feature2,
        'features3':feature3,
        'features4':feature4,
        'products1':products1,
        'products2':products2,
        'offer_product':offer_product,
    }
    
    return render(request,'./home/home.html',context)


