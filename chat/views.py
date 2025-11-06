from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# ide kell meghívni a http requestet


# chat/views.py


def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

def signup(request:HttpRequest):
    template = 'chat/signup.html'
    context = {}
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