from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        if username !="" and User.objects.filter(username=username).exists():

            user = authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                # messages.info(request,'Welcome to our Shop\nSuccessfully Login')
                return redirect("/")
            else:
                messages.info(request,'Invalid password')
                return redirect("/signup/login")
        else:
            messages.info(request,'Invalid Username')
            return redirect("/signup/login")
    return render(request,'./signup/login.html')

# Sign up page 
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != "" and password1 == password2:
            if username=="" or User.objects.filter(username=username).exists():
                messages.info(request,"This Username is already taken")
                return redirect('signup')
            elif first_name=="":
                messages.info(request,"Enter a valid First Name")
                return redirect('signup')
            elif last_name=="":
                messages.info(request,"Enter a valid Last Name")
                return redirect('signup')
            elif email=="" or User.objects.filter(email=email).exists():
                messages.info(request,"This email is already taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save();
                # messages.info(request,"Your Registration Successful")
                return HttpResponseRedirect('login/')
        else:

            messages.info(request,"Your password and confirm password does't match")
            return redirect('signup')
    return render(request,'./signup/signup.html')

#Log_out 
def Logout_user(request):
    logout(request)
    return redirect('/')


#Tracking Page. 
def tracking(request):
    return render(request,'./signup/tracking.html')