from django.urls import path, include
from . import views as group_views


urlpatterns = [
    path("create/group/", group_views.groups, name="group"),
    path("group/detail/", group_views.group_detail, name="group_detail")
]
