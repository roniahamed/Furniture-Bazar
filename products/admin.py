from django.contrib import admin
from products.models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','price','is_approve','category','discount')
    list_display_link = ('id','name')
    list_filter = ('price','category')
    list_editable = ('is_approve',)
    search_fields = ("name","price","category__name")
    ordering = ('price',)

admin.site.register(Products, ProductAdmin)

admin.site.register(Category,)