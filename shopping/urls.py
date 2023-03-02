
from django.urls import path
from . import views

app_name = 'shopping'

urlpatterns = [
    path('checkout/',views.check_out,name='checkout'),
    path('confirmation/',views.confirmation, name='confirmation'),
    path('cart/',views.cart, name='cart'),
    path('add-to-cart/<int:pk>/',views.add_to_cart, name='add_to_cart'),
    path('remove-item/<int:pk>/', views.remove_from_cart, name='remove-item'),
]
