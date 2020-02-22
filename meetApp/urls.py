from django.contrib import admin
from django.urls import path, include
from createGroup.views import groupCreate
from users.views import password, settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", groupCreate, name="groupCreate"),
    path("users/",include("users.urls")),
    path("oauth/", include("social_django.urls", namespace="social")),
    path("settings/", settings, name="settings"),
    path("settings/password/", password, name="password"),
]
