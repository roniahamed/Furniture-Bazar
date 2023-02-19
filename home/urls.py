from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='homepage')
]
