from django.shortcuts import render

# Create your views here.

# Shopping checkout section
def check_out(request):
    return render(request,'./shopping/checkout.html')

# Shopping confirmation section
def confirmation(request):
    return render(request,'./shopping/confirmation.html')