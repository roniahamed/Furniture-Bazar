from django.shortcuts import render

from products.models import *
from products.models import Products
from django.core.paginator import Paginator

from shopping.models import whitelist

# Create your views here.

# Category sector
def category(request):
    products = Products.objects.all()
    paginator = Paginator(products,6)
    page_number = request.GET.get('page')
    product_final = paginator.get_page(page_number)
    category_name = Category.objects.all()
    context = {
        'products':products,
        'product_final':product_final,
        'categories':category_name
    }
    return render(request,'products/category.html',context)


# Category filtering 
def category_filtering(request,id):
    products = Products.objects.filter(category_id = id)
    paginator = Paginator(products,6)
    page_number = request.GET.get('page')
    product_final = paginator.get_page(page_number)
    title = Category.objects.filter(id=id)
    title = '- '+ title[0].name.upper()
    
    context = {
        'products':products,
        'product_final':product_final,
        'title':title
    }
    return render(request,'products/category.html',context)
    
#single Product details
def single_product_details(request,id):
    if request.user.is_authenticated:
        single_product = Products.objects.get(id=id)
        print(single_product.name)
        white_all = whitelist.objects.filter(user=request.user,products=id)
        print(white_all)
        context={
            'single_product':single_product,
            'white_all':white_all
        }
    else:
        single_product = Products.objects.get(id=id)
        context={
            'single_product':single_product,
            
        }
    return render(request,'products/single-product.html',context)

