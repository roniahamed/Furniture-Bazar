from django.db import models
from products.models import Products
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=False, null=True)
    order_products = models.ManyToManyField(Cart)
    is_ordered= models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    paymnet_id = models.CharField(max_length=300,blank=True,null = True)
    order_id = models.CharField(max_length=300,blank=True,null = True)

    def get_total(self):
        total = 0
        for order_product in self.order_products.all():
            total += float(order_product.get_total)
            
        return total
    