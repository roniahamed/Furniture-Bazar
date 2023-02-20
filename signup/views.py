from django.shortcuts import render


# Create your views here.
def log_in(request):
    return render(request,'./signup/login.html')


def sign_up(request):
    return render(request,'./signup/signup.html')

def confirmation(request):
    return render(request,'./signup/confirmation.html')

def tracking(request):
    return render(request,'./signup/tracking.html')