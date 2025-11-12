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

def signup(request):
    template = 'chat/signup.html'
    rovid = 'Sikeres regisztráció'
    hosszu = 'Sikeresen regisztrált fiókot.'
    context = {}
    if request.user.is_authenticated:
        template = 'chat/signup.html'
        rovid = ('Már regisztrált az oldalra.') 
        hosszu = 'Sőt, be is van jelentkezve,'

    if request.method == "GET":
        template = 'chat/signup.html'
    
    if request.method == "POST": 
        for kulcs in ['email', 'password', 'username', 'last_name', 'first_name']:
            if kulcs not in request.POST.keys():
                rovid = 'Sikertelen regisztráció'
                hosszu = "A POST nem tartalmaz '{kulcs}' kulcsot"
                template = 'chat/signup.html'
                
        a_username = request.POST['username']
        az_email = request.POST['email']
        
        if not validate_email(az_email):
            rovid = 'Sikertelen regisztráció'
            hosszu = 'Ez az email-cím nem helyes. Nézze meg, nem gépelte-e el!'
            template = 'chat/signup.html'
            
        if User.objects.filter(username=a_username).exists():
            rovid = 'Sikertelen regisztráció'
            hosszu = 'Ezzel a felhasználónévvel már korábban regisztráltak fiókot ezen az oldalon. Próbálkozzon más email-címmel, vagy használja a jelszó-emlékeztető funkciót!',
            template = 'chat/signup.html'
            
        a_user = User.objects.create_user(
            username = a_username,
            password = request.POST['password'],
            email = az_email,
            last_name = request.POST['last_name'],
            first_name = request.POST['first_name'],
        )

        uj_regisztralok_csoportja, _ = Group.objects.get_or_create(name='uj_regisztralo')
        a_user.groups.add(uj_regisztralok_csoportja)
        
        context = {
        'rovid' : rovid,
        'hosszu' : hosszu,
        }
        return render(request, template, context)

    return render(request, template, context)

def loginc(request:HttpRequest):
    template = 'chat/logincg.html'
    context = {}
    return render(request, template, context)
def login(request:HttpRequest):
    template = 'chat/login.html'
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
    template = 'chat/minesweper.html'
    context = {}
    return render(request, template, context)

def kezdolap(request:HttpRequest):
    template = 'chat/kezdőlap.html'
    context = {}
    return render(request, template, context)