from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User, Group
from .models import Jatek
# ide kell meghívni a http requestet


# chat/views.py


def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

def jatekvalaszto(request:HttpRequest):
    template = 'chat/jatekvalaszto.html'
    az_osszes_jatek = Jatek.objects.all()
    context = {
        'jatekok' : az_osszes_jatek,
    }
    return render(request, template, context)
def jatekkeszito(request:HttpRequest):
    template = 'chat/jatekkeszito.html'
    context = {}
    return render(request, template, context)

def signup(request:HttpRequest):
    template = 'chat/signup.html'
    a_user = User.objects.create_user(
            username = a_username,
            password = request.POST['password'],
            email = az_email,
            last_name = request.POST['last_name'],
            first_name = request.POST['first_name'],
    )
    context = {
        'fiok' : a_user
    }
    #<button type="submit">Regisztráció</button>

    return render(request, template, context)
def loginc(request:HttpRequest):
    template = 'chat/logincg.html'
    context = {}
    return render(request, template, context)
def login(request:HttpRequest):
    template = 'chat/login.html'
    context = {}
    return render(request, template, context)

def valaszto(request:HttpRequest):
    template = 'chat/jatekvalaszto.html'
    context = {}
    return render(request, template, context)

def minesweper(request:HttpRequest):
    template = 'chat/minesweper.html'
    context = {}
    return render(request, template, context)

def kezdolap(request:HttpRequest):
    template = 'chat/kezdőlap.html'
    context = {}
    return render(request, template, context)