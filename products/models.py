from django.db import models

# Create your models here.


class Products(models.Model):
    category_choice =(
        ('sofas','Sofa'),
        ('chairs','Chairs'),
        ('tables','Tables'),
        ('storage','Storage'),
        ('beds','Beds'),
        ('mattresses','Mattresses'),
        ('dressers','Dressers'),
        ('dressers','Dressers'),
        ('nightstands','Nightstands'),
        ('desks','Desks'),
    )
    quantity = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=300,blank=True,null = True)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField( max_digits=9, decimal_places=2,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    category = models.CharField(max_length=60,choices=category_choice,blank=True,null=True)
    is_approve = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    image = models.ImageField(upload_to='product',blank=True,null=True)
    def __str__(self):
        return self.name