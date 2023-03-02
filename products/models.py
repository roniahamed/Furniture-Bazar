from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=300,blank=True,null = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=False, null=True)
    quantity = models.IntegerField(blank=True,null=True)
    discount = models.FloatField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField( max_digits=9, decimal_places=2,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    is_approve = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    image = models.ImageField(upload_to='product',blank=True,null=True)
    def __str__(self):
        return self.name