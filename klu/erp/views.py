from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login


def login(request):
    if request.method=='POST':
        docname=request.POST.get('username')
        pass1=request.POST.get('password1')

        user=authenticate(request,username=docname,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('erp:prof')
        else:
            return HttpResponse("User not found")
    return render(request, 'erp/login.html')

def prof(request):
    return render(request, 'erp/prof.html')

def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("You entered a wrong confirmation Password ")
        else:

             my_user=User.objects.create_user(uname,email,pass1)
             my_user.save()
             return redirect('erp:first')



    return render(request, 'erp/register.html')

def first(request):
    if request.method=='POST':
        urname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')

        user=authenticate(request,username=urname,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('erp:doc')
        else:
            return HttpResponse("User not found")

    return render(request,'erp/first.html')
def doc(request):
    return render(request,'erp/doc.html')

def home(request):
    return render(request,'erp/home.html')
def sigin(request):
    return render(request, 'erp/sigin.html')

def prof(request):
    return render(request, 'erp/prof.html')

def about(request):
    return render(request,'erp/about.html')

def service(request):
    return render(request,'erp/service.html')

def contact(request):
    return render(request,'erp/contact.html')

def first(request):
    return render(request,'erp/first.html')

def book(request):
    return render(request,'erp/book.html')

def chat(request):
    return render(request,'erp/chat.html')


