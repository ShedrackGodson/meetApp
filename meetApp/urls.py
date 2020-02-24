from django.contrib import admin
from django.urls import path, include
from home.views import home
from users.views import password, settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("users/",include("users.urls")),
    path("oauth/", include("social_django.urls", namespace="social")),
    path("settings/", settings, name="settings"),
    path("settings/password/", password, name="password"),
]
