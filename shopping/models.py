from django.db import models
from products.models import Products
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings


# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE, default=False, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=False, null=True)
    quantity = models.IntegerField(default=1)
    is_parchased = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_updated = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return f"{self.quantity} X {self.product}"
    
    def get_total(self):
        total = self.product.price * self.quantity
        float_total = format(total, '0.2f')
        return float_total
    
    
    def get_discount(self):
        price = float(self.get_total())
        main_discount = self.product.discount / 100
        discount =  price * main_discount
        float_discount = format(discount, '0.2f')
        return float_discount
    
class Order(models.Model):
    PAYMENT_METHOD = (
        ('Cash on Delivery' , 'Cash on Delivery'),
        ('Paypal' , 'Paypal'),
        ('SSLcommerz' , 'SSLcommerz'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=False, null=True)
    order_products = models.ManyToManyField(Cart)
    is_ordered= models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    payment_id = models.CharField(max_length=300,blank=True,null = True)
    order_id = models.CharField(max_length=300,blank=True,null = True)
    payment_method = models.CharField(max_length=30,choices=PAYMENT_METHOD,default='Paypal')

    def get_totals(self):
        total = 0
        for order_product in self.order_products.all():
            total += float(order_product.get_total)
            
        return total


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} billing address"

    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.get_fields()]
        for field_name in field_names:
            value = getattr(self, field_name)
            if value is None or value=='':
                return False
        return True

    class Meta:
        verbose_name_plural = "Billing Addresses"
    