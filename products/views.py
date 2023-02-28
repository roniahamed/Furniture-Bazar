from django.shortcuts import render

from products.models import Products

# Create your views here.

# Category sector
def category(request):
    products = Products.objects.all()
    context = {
        'products':products
    }
    return render(request,'products/category.html',context)
    
#single Product details
def single_product(request):
    return render(request,'products/single-product.html')

