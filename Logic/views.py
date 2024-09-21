from django.shortcuts import render, HttpResponse
from . import forms
# Create your views here.

users = []

def dataAction(request, action, **kwargs):
    """Форма регистрации/авторизации"""
    get = request.GET
    user = {
        "username" : get.get("username", ""),
        "password" : get.get("password", ""),
        "email" : get.get("email", "")
    }
    context = {
        "entry" : forms.Entry
    }
    I = render(request, "myPage.html", user)

    if all(user.values()): #* не пустые строки
        if action == "registration":
            if user not in users:
                users.append(user)
                return I
            return HttpResponse("Вы уже зарегистрированы")
        
        elif action == "authorization":
            if user in users:
                return I
            return HttpResponse("Вы ещё не зарегистрировались")
            
    return render(request, action + ".html", context)