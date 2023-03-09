from django.db.models import Q
from django.shortcuts import render
from products.models import *
from django.core.paginator import Paginator


# Create your views here.

def search_ing(request):
    get_method = request.GET.copy()
    keywords = get_method.get('keywords') or None
    if keywords:
        keyword = get_method['keywords']
        list_product = Products.objects.filter(Q(name__icontains=keyword) | Q(title__icontains=keyword) | Q(category__name=keyword) | Q(image__icontains=keyword))
        paginator = Paginator(list_product,6)
        page_number = request.GET.get('page')
        product_final = paginator.get_page(page_number)
    category_name = Category.objects.all()
    
    context = {
        'list_product':list_product,
        'product_final':product_final,
        'value':keyword,
        'categories':category_name,
    }
    return render(request,'search_result/searching.html',context)