from django.shortcuts import render

from products.models import Products
from django.core.paginator import Paginator

# Create your views here.

# Category sector
def category(request):
    products = Products.objects.all()
    paginator = Paginator(products,6)
    page_number = request.GET.get('page')
    product_final = paginator.get_page(page_number)
    # products =Products.objects.all().order_by('-date_added')[:9]
    context = {
        # 'products':products,
        'product_final':product_final
    }
    return render(request,'products/category.html',context)
    
#single Product details
def single_product_details(request,id):
    single_product = Products.objects.get(id=id)
    context={
        'single_product':single_product
    }
    return render(request,'products/single-product.html',context)

