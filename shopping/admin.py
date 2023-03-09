from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(BillingAddress)
admin.site.register(whitelist)
