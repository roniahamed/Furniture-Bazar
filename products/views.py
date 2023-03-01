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
def single_product_details(request,id):
    single_product = Products.objects.get(id=id)
    context={
        'single_product':single_product
    }
    return render(request,'products/single-product.html',context)

