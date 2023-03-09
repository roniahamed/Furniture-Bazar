from django.db import models
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile/',blank=True,null=True)
    about = models.CharField(max_length=30,blank=True,null=True)
    mobile = models.CharField(max_length=150,blank=True,null=False)
    address = models.CharField(max_length=150,blank=True,null=False)
