from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


from .models import Department,Doctors,Booking
from .forms import *

#Create your views here.
def base(request):
    # return HttpResponse("Home page")

    person={
        'name': 'Teena',
        'age': 20,
        'place': 'aluva'
    }
    return render(request, "base.html",person)
def about(request):
    # return HttpResponse("Home page")
    numb={
        'num1': 10
    }
    return render(request,"about.html",numb)
def contact(request):
    form=contactform
    mydict={
        "form":form
    }
    return render(request, "contacts.html" ,mydict)

def department(request):
    # return HttpResponse("Home page")
    dict_dep={
        'depkey':Department.objects.all()
    }
    return render(request, "department.html" ,dict_dep)
def doctors(request):
    dict_docs={
        'dockey':Doctors.objects.all()
    }
    return render(request,"doctors.html",dict_docs)
def career_view(request):
    form=careerform
    mydict={
        "form":form,
        'jobkey': Job.objects.all()
    }
    return render(request,"career.html",mydict)


def booking(request):
    form=BookingForm
    mydict = {
        "form": form
    }
    return render(request,"booking.html",context=mydict)

def first(request):
    return render(request,"main.html")

# def my_view(request):
#     for i in login_user:
#         messages.success(request,"Welcome, {i.username} ")




def signup(request):
    if request.method == 'POST':
        # print(type(request.POST))
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pswrd')
        cpass = request.POST.get('cnfrmpswrd')
        if not username or not email or not password or not cpass:
            messages.add_message(request,messages.ERROR,'All fields Required')
        else:
                if User.objects.filter(username=username).exists():
                    messages.add_message(request,messages.ERROR, 'Username Already Exists')
                    return HttpResponseRedirect(reverse('signup'))
                elif User.objects.filter(email=email).exists():
                    messages.add_message(request,messages.ERROR,'Email Already Exists')
                    return HttpResponseRedirect(reverse('signup'))
                elif password!=cpass:
                    messages.add_message(request,messages.ERROR,'Password do not match.')
                    return HttpResponseRedirect(reverse('signup'))
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return HttpResponseRedirect(reverse('login'))
                    # return render(request,"login.html")

        return render(request, "signup.html")
    else:
        print("hhh")
        return render(request,"signup.html")


def login_user(request):
    if request.method == 'POST':
        print(type(request.POST))
        username = request.POST.get('username')
        password = request.POST.get('pswrd')
        if not username or not password:
            messages.add_message(request,messages.ERROR,'All fields Required')
        else:
            user = auth.authenticate(request,username=username, password=password)
            if user is not None:
                welcome_msg=f"Hello, {username}!"
                return render(request,"base.html",{'welcome_msg':welcome_msg})
            else:
                messages.add_message(request, messages.ERROR, 'Invalid username or password')
                return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, "login.html")

#
# def logout(request):
#     auth.logout(request)
#     return redirect('home')