from itertools import product
from django.shortcuts import render
from products.models import Products
from products.views import category
# Create your views here.

def home_page(request):
    
    slider = Products.objects.filter(category_id=1)
    # feature =Products.objects.filter(category='sofas')
    products1 =Products.objects.all().order_by('-date_added')[:8]
    
    context = {
        'slider':slider,
        # 'features':feature,
        'products1':products1,
       
    }
    
    return render(request,'./home/home.html',context)


