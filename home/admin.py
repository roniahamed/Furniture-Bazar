from django.contrib import admin
from .models import *
# Register your models here.
class SlideAdmin(admin.ModelAdmin):
    list_display=('id','title','price','is_approve')
    list_editable = ('is_approve',)
    ordering = ('price',)

admin.site.register(Slide,SlideAdmin)