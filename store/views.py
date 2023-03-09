from django.shortcuts import render
from shopping.models import *
from django.core.paginator import Paginator
# Create your views here.
def wish_list(request):
    if request.user.is_authenticated:
        products = whitelist.objects.filter(user=request.user)
        paginator = Paginator(products,6)
        page_number = request.GET.get('page')
        product_final = paginator.get_page(page_number)
        context = {
            'products':products,
            'product_final':product_final,
        }
    return render(request,'./wishlist/wishlist.html',context)