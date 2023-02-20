from django.urls import path
from . import views


urlpatterns = [
    path('',views.log_in,name='logpage'),
    path('signup',views.sign_up,name='signup'),
   
]
