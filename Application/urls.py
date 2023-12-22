from django.urls import path
from . import views
urlpatterns = [
    path('',views.twoButtons),
    path('teachersignup/', views.teacherSignup, name='teacherSignup'),
    path('studentsignup/', views.studentSignup, name='studentSignup'),
    path('teacherlogin/',views.teacherLogin,name='teacherLogin'),
    path('studentlogin/',views.studentLogin,name='studentLogin'),
]