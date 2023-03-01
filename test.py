from django.shortcuts import render,get_object_or_404,redirect
from products.models import Products
from shopping.models import Cart,Order
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

# Create your views here.

@login_required
def add_to_cart(request,pk):
    product = get_object_or_404(Products, pk=pk)
    order_product = Cart.objects.get_or_create(product = product,user=request.user, is_parchased = False)
    order_qs = Order.objects.filter(user=request.user, is_ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_products.filter(product = product).exists():
            order_product[0].quantity += 1
            order_product[0].save()
            return redirect('shopping:cart')
        else:
            order.order_products.add(order_product[0])
            return redirect('shopping:cart')
    else:
        order = Order(user=request.user)
        order.save()
        order.order_products.add(order_product[0])
        return redirect('shopping:cart')


# Shopping checkout section
def check_out(request):
    return render(request,'./shopping/checkout.html')

# Shopping confirmation section

def cart(request):
    if request.user.is_authenticated():
        cart_product = Cart.objects.filter(user=request.user)
    return render(request,'./shopping/cart.html')


# Shopping confirmation section
def confirmation(request):
    return render(request,'./shopping/confirmation.html')