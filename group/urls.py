from django.urls import path, include
from . import views


urlpatterns = [
    path("create/group/", views.groups, name="group"),
    path("group/detail/<int:pk>/", views.GroupDetailView.as_view(), name="group-detail"),
    # path("group/detail/", group_views.group_detail, name="group_detail")
]
