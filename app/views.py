from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Customers_Details
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        datas=Customers_Details.objects.all()
        c=Customers_Details.objects.all().count()
        return render(request,'index.html',{'data':datas,'count':c})     

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,"Please provide right credentials!")
            return redirect('login')
    return render(request,'login.html') 

def forget(request):
    if request.method=='POST':
        name=request.POST.get('email')
        print(name)
        confirm=messages.success(request,'Username & Password will send on admin email. Click Here to')
    return render(request,'forget.html')


def customer(request,val):
    tab=Customers_Details.objects.get(id=val)
    if request.method=='POST':
        name=request.POST.get('nam')
        detail1=request.POST.get('detail1')
        detail2=request.POST.get('detail2')
        detail3=request.POST.get('detail3')
        detail4=request.POST.get('detail4')
        submit=Customers_Details(id=val,c_name=name,detail1=detail1,detail2=detail2,detail3=detail3,detail4=detail4,date=datetime.today())
        submit.save()
        confirm=messages.success(request,'Data Updated Successfully!')
    return render(request,'customer.html',{'data':tab})

def delete(request,id):
    tab=Customers_Details.objects.get(id=id).delete()
    return redirect('/')

def addc(request):
    if request.method=='POST':
        c_name=request.POST.get('name')
        detail1=request.POST.get('d1')
        detail2=request.POST.get('d2')
        detail3=request.POST.get('d3')
        detail4=request.POST.get('d4')
        if Customers_Details.objects.filter(c_name=c_name).exists():
            messages.error(request,'This Customer name was already exist!')
            return redirect('addc')
        else:
            submit=Customers_Details(c_name=c_name,detail1=detail1,detail2=detail2,detail3=detail3,detail4=detail4,date=datetime.today())
            submit.save()
            messages.success(request,'Customer Added Successfully')
    return render(request,'add_customer.html')

def about(request):
    return render(request,'about.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

def search(request):
    if request.method=='POST':
        query=request.POST.get('value')
        post=Customers_Details.objects.filter(c_name__icontains=query)
        c=Customers_Details.objects.filter(c_name__icontains=query).count()
        confirm=messages.success(request,'Your current search result is: '+str(c))
        return render(request,'search.html',{'data':post})
    return render(request,'search.html')