from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='teacherLogin')
@login_required(login_url='studentLogin')

def twoButtons(request):
    return render(request,'Application/home.html')

def teacherSignup(request):
    if request.method=='POST':
        uname=request.POST.get('Tusername')
        email=request.POST.get('Temail')
        pass1=request.POST.get('Tpassword1')
        pass2=request.POST.get('Tpassword2')
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('teacherLogin')
    return render (request,'Application/teachersignup.html')

def teacherLogin(request):
    if request.method=='POST':
        username=request.POST.get('Tusername')
        pass1=request.POST.get('Tpass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request,'Application/teacherlogin.html')

def studentSignup(request):
    if request.method=='POST':
        uname=request.POST.get('Susername')
        email=request.POST.get('Semail')
        pass1=request.POST.get('Spassword1')
        pass2=request.POST.get('Spassword2')
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_userr=User.objects.create_user(uname,email,pass1)
            my_userr.save()
            return redirect('studentLogin')
    return render (request,'Application/studentsignup.html')

def studentLogin(request):
    if request.method=='POST':
        username=request.POST.get('Susername')
        pass1=request.POST.get('Spass')
        userr=authenticate(request,username=username,password=pass1)
        if userr is not None:
            login(request,userr)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request,'Application/studentlogin.html')