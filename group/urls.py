from django.urls import path, include
from . import views as group_views


urlpatterns = [
    path("group/", group_views.groups, name="group")
]
