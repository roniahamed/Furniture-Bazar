from django.shortcuts import render

# Create your views here.

# Category sector
def category(request):
    return render(request,'products/category.html')


#single Product details
def single_product(request):
    return render(request,'products/single-product.html')

