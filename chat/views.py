from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# ide kell meghívni a http requestet


# chat/views.py


def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

def valaszto(request:HttpRequest):
    template = 'chat/jatekvalaszto.html'
    context = {}
    return render(request, template, context)

def minesweper(request:HttpRequest):
    template = 'chat/minesweper.html'
    context = {}
    return render(request, template, context)
    