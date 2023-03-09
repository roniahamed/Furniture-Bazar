from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from user.models import Profile
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            about = request.POST['about']
            mobile = request.POST['phone']
            address = request.POST['address']
            updated_password = request.POST['updated_password']
            password = request.POST['previous_password']
            user = request.user
            user1 = authenticate(username=user.username,password=password)
            if user1:
                profile = Profile.objects.filter(user=request.user)
                if profile:
                    profile.update(about = about)
                    profile.update(mobile = mobile)
                    profile.update(address = address)
                else:
                    profile = Profile(user=request.user,about=about,mobile=mobile,address=address)
                    profile.save()
                if updated_password != "":
                    if len(updated_password) >= 5:
                        U = User.objects.get(username=request.user.username)
                        U.set_password(updated_password)
                        U.save()
                        messages.info(request,'Password Change successful')
                    else:
                        messages.info(request,'Password is very short')
                
            else:
                messages.info(request,'Invalid password')
        user = request.user
        profile = Profile.objects.filter(user=request.user)
        if profile:
            profile = profile[0]
        context={
            'user':user,
            'profile':profile,
        }
    return render(request, 'user/user.html',context)