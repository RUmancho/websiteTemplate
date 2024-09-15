from django.shortcuts import render
from . import forms
# Create your views here.

users = []

def registration(request):
    """Форма регистрации"""
    entry = forms.RegistrationForm()

    email = request.POST.get('email', "")
    password = request.POST.get('password', "")
    username = request.POST.get('username', "")

    context = {
        "entry": entry,
        "username" : username
    }

    if not all([email, password, username]):
        return render(request, "registration.html", context)
    
    users.append({
        "email" : email,
        "password" : password,
        "username" : username
    })

    return render(request, "myPage.html", context)

def autorization(request):
    """Форма авторизации"""
    entry = forms.RegistrationForm()

    email = request.POST.get('email', "")
    password = request.POST.get('password', "")
    username = request.POST.get('username', "")

    context = {
        "username" : username,
        "entry"    : entry
    }

    getAutorisateData = {
        "email":    email,
        "password": password,
        "username": username
    }

    if getAutorisateData in users:
        return render(request, "myPage.html", context)
    
    return render(request, "authorization.html", context)