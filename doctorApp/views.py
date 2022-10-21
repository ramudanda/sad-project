import email
from multiprocessing import context
from sched import scheduler
from sqlite3 import Date, Time
from unicodedata import name
from urllib import request
from django.views import generic
from .models import *
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

def home(request):
    context={}
    return render(request, 'index.html', context)

def appointment(request):
    apbk = Appointment.objects.all()
    return render(request, 'appointment.html', context={'apbk':apbk})


           # if request.method =='POST'and 'apointbtn' in request.POST:
    #     print(Date)
    #     form.save()
    #     messages.success(request, 'Appointment submitted')
@login_required(login_url='login')
def book(request):
    
    
    if request.method == 'POST':
        Name=request.POST['Name']
        email=request.POST['email']
        Phone =request.POST['Phone']
        Date=request.POST['Date']      
        Doctor=request.POST['Doctor']
        Schedule=request.POST['Schedule']
        Disease =request.POST['Disease']
        booking=Appointment.objects.create(Name=Name,email=email,Date=Date, Time=Time, Phone=Phone,  Doctor=Doctor, Schedule=Schedule, Disease=Disease)   
    return render(request, 'book.html', context={ })
     
    

def registrationPage(request):
    form =CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() 
            user = form.cleaned_data.get('username')
            messages.success(request, 'Acccount created for ' +user)
            return redirect('login')

    context={'form':form}
    return render(request,  'accounts/register.html', context)

# def appointment(request):
#     if request.method=="POST":
#         Name = request.POST['Name']
#         # Emails = request.POST['Emails']
#         schedule = request.POST['schedule']
#         Time = request.POST['Time']
#         Date = request.POST['Date']
#         Phone = request.POST['Phone']

#         return render(request, 'accounts/login.html', {
#         'Name': Name,
#         # 'Email':Emails,
#         'Time':Time,
#         'Date':Date,
#         'schedule':schedule,
#         'Phone':Phone})


#     else:   
#         return render(request, 'accounts/login.html' ,context)



def loginpage(request):
    if request.method =='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('book')
        else:
            messages.info(request, "Username/Password is Incorrect")

    context={}
    return render(request,'accounts/login.html', context)


def appointment(request):
    apbk = Appointment.objects.all()
    return render(request, 'book.html', context={'apbk':apbk})