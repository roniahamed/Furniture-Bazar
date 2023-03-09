from django.shortcuts import render

# Create your views here.

def user(request):
    return render(request, 'user/user.html')