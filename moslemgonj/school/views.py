from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def jbhs(request):
    return render (request,'jbhs.html')
def mhs(request):
    return render (request,'mhs.html')


def login(request):
    if request.method=='POST':
        username=request.POST.get("username")
        pass1=request.POST.get("pass1")
        user=authenticate(request,username=username,password1=pass1)
        if user is not None:
            login(request,user)
            return redirect('mhs')
        else:
            return HttpResponse("you are worng")
        


    return render (request,'login.html')
def singup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1!=password2:
            return HttpResponse("Your Password and Confrom Password are not same!!")
        else:

            my_user=User.objects.create_user(uname,email,password1)
            my_user.save()
            return redirect('login')

    return render (request,'singup.html')