from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def twoButtons(request):
    return render(request,'Application/home.html')

def teacherSignup(request):
    return render(request,'Application/teachersignup.html')

def teacherLogin(request):
    return render(request,'Application/teacherlogin.html')

def studentSignup(request):
    return render(request,'Application/studentsignup.html')

def studentLogin(request):
    return render(request,'Application/studentlogin.html')