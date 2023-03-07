from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from products.models import Products
from shopping.models import Cart,Order,BillingAddress
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views.generic import TemplateView



# Create your views here.

def add_to_cart(request,pk):
    product = get_object_or_404(Products, pk=pk)
    order_product = Cart.objects.get_or_create(product = product,user=request.user, is_parchased = False)
    order_qs = Order.objects.filter(user=request.user, is_ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_products.filter(product = product).exists():
            order_product[0].quantity += 1
            order_product[0].save()
            messages.info(request, "This product quantity was updated!")
            return redirect('shopping:cart')
        else:
            order.order_products.add(order_product[0])
            messages.info(request, "This product was added to your cart!")
            return redirect('shopping:cart')
    else:
        order = Order(user=request.user)
        order.save()
        order.order_products.add(order_product[0])
        messages.info(request, "This product was added to your cart!")
        return redirect('shopping:cart')
    
    
@login_required  
def remove_from_cart(request, pk):
    product = get_object_or_404(Products, pk=pk)
    order_qs = Order.objects.filter(user=request.user, is_ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_products.filter(product=product).exists():
            order_product = Cart.objects.filter(product=product, user=request.user, is_parchased=False)[0]
            order.order_products.remove(order_product)
            order_product.delete()
            messages.warning(request, "This item was remove from your cart!")
            return redirect('shopping:cart')
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('shopping:cart')
    else:
        messages.info(request, "You don't have an active order")
        return redirect('shopping:cart')
    
@login_required
def increase_cart(request, pk):
    product = get_object_or_404(Products, pk=pk)
    order_qs = Order.objects.filter(user=request.user, is_ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_products.filter(product=product).exists():
            order_product = Cart.objects.filter(product=product, user=request.user, is_parchased=False)[0]
            if order_product.quantity >= 0:
                order_product.quantity += 1
                order_product.save()
                messages.info(request, f"{product.name} quantity has been updated")
                return redirect('shopping:cart')
            else:
                messages.info(request, f"{product.name} is not in your cart")
                return redirect('shopping:cart')
        else:
            messages.info(request, "You don't have an active order")
            return redirect('shopping:cart')
        

@login_required
def  decrease_cart(request, pk):
    product = get_object_or_404(Products, pk=pk)
    order_qs = Order.objects.filter(user=request.user, is_ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_products.filter(product=product).exists():
            order_product = Cart.objects.filter(product=product, user=request.user, is_parchased=False)[0]
            if order_product.quantity  != 1 :
                order_product.quantity -= 1
                order_product.save()
                messages.info(request, f"{product.name} quantity has been updated")
                return redirect('shopping:cart')
            else:
                order.order_products.remove(order_product)
                order_product.delete()
                messages.info(request, f"{product.name} is not in your cart")
                return redirect('shopping:cart')
        else:
            messages.info(request, f"{product.name} is not in your cart")
            return redirect('shopping:cart')
    else:
        messages.info(request, "You don't have an active order")
        return redirect('shopping:index')
    
        


    

# Shopping checkout section
def checkout(request):
 
    if request.user.is_authenticated:
        if request.method == 'POST':
            first = request.POST['first']
            last = request.POST['last']
            number = request.POST['number']
            email = request.POST['email']
            add1 = request.POST['add1']
            add2 = request.POST['add2']
            city = request.POST['city']
            zip = request.POST['zip']
            payment_method = request.POST['payment']
            billing_address = BillingAddress(user=request.user, first_name = first,last_name = last,phone_number = number,email_address =email,address =add1,address2 =add2,city =city,zipcode =zip,)
            pay_method = Order(user=request.user, payment_method = payment_method,)
            billing_address.save()
            pay_method.save()
            if pay_method.payment_method == 'Cash On Delivery':
                order_qs = Order.objects.filter(user=request.user, is_ordered=False)
                order = order_qs[0]
                order.is_ordered = True
                order.order_id = order.id
                order.payment_id = pay_method.payment_method
                order.save()
                cart_items = Cart.objects.filter(user=request.user, is_parchased=False)
                for item in cart_items:
                    item.is_parchased = True
                    item.save()
                    print('Order Submitted Successfully')  
        carts = Cart.objects.filter(user=request.user)
        sub_total = 0
        quantity = 0
        discount = 0
        total = 0
        delivery = 0

        for cart in carts:

            sub_total += float(cart.get_total())
            discount += float(cart.get_discount())
            quantity += int(cart.quantity)

        if sub_total:
            delivery = 15

        total = sub_total-discount+delivery
                
                # print (carts.get_total())
        context = {
            'carts':carts,
            'sub_total': sub_total,
            'quantity': quantity,
            'discount': discount,
            'delivery' :delivery,
            'total' : total,
            }
            
    else:
        return redirect("/signup/login")
    return render(request,'./shopping/checkout.html',context)


# Shopping confirmation section

def cart(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user,is_parchased=False)
        sub_total = 0
        quantity = 0
        discount = 0
        total = 0
        delivery = 0

        for cart in carts:

            sub_total += float(cart.get_total())
            discount += float(cart.get_discount())
            quantity += int(cart.quantity)

        if sub_total:
            delivery = 15

        total = sub_total-discount+delivery
        
        # print (carts.get_total())
        context = {
            'carts':carts,
            'sub_total': sub_total,
            'quantity': quantity,
            'discount': discount,
            'delivery' :delivery,
            'total' : total,

        }
    else:
        return redirect("/signup/login")
    return render(request,'./shopping/cart.html',context)


# Shopping confirmation section
def confirmation(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user,is_parchased=True)
        order_qs = Order.objects.filter(user=request.user, is_ordered = True)
        b_add = BillingAddress.objects.filter(user=request.user)
        address = b_add[len(b_add)-1]
        order = order_qs[len(order_qs)-1]
        sub_total = 0
        quantity = 0
        discount = 0
        total = 0
        delivery = 0

        for cart in carts:

            sub_total += float(cart.get_total())
            discount += float(cart.get_discount())
            quantity += int(cart.quantity)

        if sub_total:
            delivery = 15

        total = sub_total-discount+delivery
        
        # print (carts.get_total())
        context = {
            'carts':carts,
            'sub_total': sub_total,
            'quantity': quantity,
            'discount': discount,
            'delivery' :delivery,
            'total' : total,
            'order' : order,
            'address' : address,

        }
    else:
        return redirect("/signup/login")

    return render(request,'./shopping/confirmation.html',context)


