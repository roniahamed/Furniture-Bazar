from django.shortcuts import render

from products.models import *

# Create your views here.

# Category sector
def category(request):
    products =Products.objects.all().order_by('-date_added')[:9]
    category_name = Category.objects.all()
    context = {
        'products':products,
        'categories':category_name
    }
    return render(request,'products/category.html',context)


# Category filtering 
def category_filtering(request,id):
    products =  products =Products.objects.filter(category_id = id)
    title = Category.objects.filter(id=id)
    title = '- '+ title[0].name.upper()
    
    context = {
        'products':products,
        'title':title
    }
    return render(request,'products/category.html',context)
    
#single Product details
def single_product_details(request,id):
    print(id)
    single_product = Products.objects.get(id=id)
    context={
        'single_product':single_product
    }
    return render(request,'products/single-product.html',context)

