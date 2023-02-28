from django.shortcuts import render

from products.models import Products

# Create your views here.

# Category sector
def category(request):
    return render(request,'products/category.html')

def all_product(request):
    products = Products.objects.all()
    context = {
        'products':products
    }
    
#single Product details
def single_product(request):
    return render(request,'products/single-product.html')

