from django.db import models

# Create your models here.
class Slide(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    short_description = models.CharField(max_length=200,blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField( max_digits=9, decimal_places=2,blank=True,null=True)
    is_approve = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    width = models.CharField(max_length=30,blank=True,null = True)
    height = models.CharField(max_length=30,blank=True,null = True)
    depth = models.CharField(max_length=30,blank=True,null = True)
    weight = models.CharField(max_length=30,blank=True,null = True)
    quality_checking = models.CharField(max_length=30,blank=True,null = True)
    image = models.ImageField(upload_to='product',blank=True,null=True)
    def __str__(self):
        return self.title