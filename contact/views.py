from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
# Create your views here.
def contact_info(request):
    if request.method == 'POST':
        mess_age = request.POST['mess_age']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        admin = "mdroniahamed56@gmail.com"
        print(name)
        print(mess_age)
        print(email)
        body = {
            'name':name,
            'email':email,
            'message':mess_age,
        }
        message = '\n'.join(body.values())
        if subject and name and mess_age and email:
            send_mail(subject,mess_age,email,[admin])
        # # except BadHeaderError:
        # #     return HttpResponse('Invalid header found')
        # return redirect('/')
    return render(request,'contact/contact.html')