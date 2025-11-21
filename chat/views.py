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


   
       
# def valaszto(request:HttpRequest):
#     template = 'chat/jatekvalaszto.html'
#     # jelenlegfutó_játékok = Jatek.objects.all()
#     # context = {
#         # 'jatekok' : jelenlegfutó_játékok,
#     # }
#     context = {}
#     return render(request, template, context)

def minesweper(request:HttpRequest):
    template = 'chat/indexx.html'
    context = {}
    return render(request, template, context)

def kezdolap(request:HttpRequest):
    template = 'chat/kezdőlap.html'
    context = {}
    return render(request, template, context)