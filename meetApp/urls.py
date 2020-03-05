from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from home.views import home,password
# from users.views import password, setting
from django.conf.urls.static import static
from django.views.static import serve
from group import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("users/",include("users.urls")),
    path("",include("group.urls")),
    path("",include("home.urls")),
    path("oauth/", include("social_django.urls", namespace="social")),
    path("settings/", home, name="settings"),
    path("settings/password/", password, name="password"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)