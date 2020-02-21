from django.contrib import admin
from django.urls import path
from createGroup.views import groupCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", groupCreate, name="groupCreate"),
]
