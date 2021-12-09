from django.shortcuts import render,redirect,HttpResponse
from .models import *
import bcrypt
from django.contrib import messages
from datetime import datetime


def mainpage(request):
    context = {

    }
    return render(request,"mainpage.html",context)

# def success(request):
#     user_id = request.session.get('user_id')
#     if user_id:
#         context = {
#             'user' : User.objects.get(id=user_id)
#         }
#         return render(request,"success.html",context)
#     else:
#         return redirect('/')

def register(request):
    errors = User.objects.registerValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birthday = request.POST['birthday']
        email = request.POST['email']
        password = request.POST['password']
        password_bcrypt = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        user = User.objects.create(first_name=first_name,last_name=last_name,birthday=birthday,email=email,password=password_bcrypt)
        request.session['user_id'] = user.id
        return redirect('/wall')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)[0]
        request.session['user_id'] = user.id
        return redirect('/wall')
    


def logout(request):
    request.session.flush()
    return redirect('/')

