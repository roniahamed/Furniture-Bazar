from django.urls import path
from . import views

urlpatterns = [
    path('',views.category, name='category'),
    path('category/<int:id>',views.category_filtering, name='category_filtering'),
    path('single_product/<int:id>',views.single_product_details,name='single_product')
]
