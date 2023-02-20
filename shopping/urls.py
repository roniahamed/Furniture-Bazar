
from django.urls import path
from . import views

urlpatterns = [
    path('checkout/',views.check_out,name='checkout'),
    path('confirmation/',views.confirmation, name='confirmation')
]
