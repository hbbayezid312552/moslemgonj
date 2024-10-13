from django.shortcuts import render
from django.http import HttpResponse
from mhs1.models import Contact


# Create your views here.
def basic(request):
    return render (request,'basic.html')

def deshboard(request):
    return render (request,'home.html')

def home(request):
    return render (request,'home.html')

def about(request):
    return render (request,'about.html')

def blog(request):
    return render (request,'blog.html')
    
def contact(request):
    if request.method=="POST":
        name =request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        disc =request.POST['disc']
        vlues=Contact(name=name,email=email,phone=phone,disc=disc)
        vlues.save()
    return render (request,'contact.html')


   
   

