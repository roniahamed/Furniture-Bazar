
from django.urls import path
from . import views

app_name = 'shopping'

urlpatterns = [
    path('checkout/',views.checkout,name='checkout'),
    path('confirmation/',views.confirmation, name='confirmation'),
    path('cart/',views.cart, name='cart'),
    path('add-to-cart/<int:pk>/',views.add_to_cart, name='add_to_cart'),
    path('remove-item/<int:pk>/', views.remove_from_cart, name='remove-item'),
    path('increase-item/<int:pk>/', views.increase_cart, name='increase-item'),
    path('decrease-item/<int:pk>/', views.decrease_cart, name='decrease-item'),
    path('whitelist/<int:pk>/', views.whitelist, name='whitelist'),
]
