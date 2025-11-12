# mysite/urls.py
from django.contrib import admin
from django.urls import include, path
from chat.views import *

urlpatterns = [
    path("chat/", include("chat.urls")),
    path("admin/", admin.site.urls),
    path("minesweper/", minesweper),
    path("", kezdolap),
    path("signup", signup),
    path("login", login),
    path("loginc",loginc),
    path("jatekvalaszto",jatekvalaszto),
    path("jatekkeszito",jatekkeszito),
]