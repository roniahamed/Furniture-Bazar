from django import template
from shopping.models import Cart,Order

register = template.Library()

@register.filter()
def cart_view(user):
    cart = Cart.objects.filter(user = user, is_parchased = False)
    if cart.exists():
        return cart
    else:
        return ValueError("You haven't an active cart.")
    
@register.filter
def cart_total(user):
    order = Order.objects.filter(user=user, is_ordered=False)
    if order.exists():
        return order[0].order_products.count()
    else:
        return 0

