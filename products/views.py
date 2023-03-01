from django.shortcuts import render

from products.models import Products

# Create your views here.

# Category sector
def category(request):
    products = Products.objects.all()
    products =Products.objects.all().order_by('-date_added')[:9]
    context = {
        'products':products
    }
    return render(request,'products/category.html',context)
    
#single Product details
def single_product_details(request,id):
    single_product = Products.objects.get(id=id)
    context={
        'single_product':single_product
    }
    return render(request,'products/single-product.html',context)

