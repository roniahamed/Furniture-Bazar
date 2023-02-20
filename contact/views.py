from django.shortcuts import render

# Create your views here.
def contact_info(request):
    return render(request,'contact/contact.html')