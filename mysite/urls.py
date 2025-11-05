# mysite/urls.py
from django.contrib import admin
from django.urls import include, path
from chat.views import minesweper
from chat.views import kezdolap
from chat.views import signup
from chat.views import login

urlpatterns = [
    path("chat/", include("chat.urls")),
    path("admin/", admin.site.urls),
    path("minesweper/", minesweper),
    path("", kezdolap),
    path("signup", signup),
    path("login", login),
]