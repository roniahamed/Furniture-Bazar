from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.log_in,name='logpage'),
    path('',views.sign_up,name='signup'),
    path('tracking/',views.tracking,name='tracking'),
]
