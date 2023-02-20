from django.shortcuts import render

# Create your views here.
def check_out(request):
    return render(request,'./shopping/checkout.html')
