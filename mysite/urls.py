# mysite/urls.py
from django.contrib import admin
from django.urls import include, path
from chat.views import minesweper

urlpatterns = [
    path("chat/", include("chat.urls")),
    path("admin/", admin.site.urls),
    path("minesweper/", minesweper),
]