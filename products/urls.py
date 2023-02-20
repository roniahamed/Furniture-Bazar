from django.urls import path
from . import views

urlpatterns = [
    path('',views.category, name='category'),
    path('single_product/',views.single_product,name='single_product')
]
