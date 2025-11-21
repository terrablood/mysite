# mysite/urls.py
from django.contrib import admin
from django.urls import include, path
from chat.views import *
from app_reg.views import *

urlpatterns = [
    path("chat/", include("chat.urls")),
    path("admin/", admin.site.urls),
    path("minesweper/", minesweper),
    path("", kezdolap),
    path('minesweper',minesweper),
    
    path("jatekvalaszto",jatekvalaszto),
    path("jatekkeszito",jatekkeszito),
    path("regisztracio",regisztracio),
    
]