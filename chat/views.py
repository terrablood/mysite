from django.shortcuts import render



# chat/views.py


def index(request):
    return render(request, "chat/index.html")