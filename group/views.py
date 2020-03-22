from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.views import locationTracer
from users.models import Profile
from .models import Topics, MeetAppGroup
from .forms import GroupCreationForm
from django.views.generic import DetailView


@login_required
def groups(request):
    context = {
        
    }
    # location = locationTracer()
    # context["location"] = location
    group_topics = Topics.objects.all()[0:23]
    context["topics"] = group_topics
    form = GroupCreationForm(request.POST)
    user = request.user

    if request.method=="POST":
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Group Created.")
            return redirect("/")
        else:
            form = GroupCreationForm(request.POST)
            print("Group not created.")
            return redirect("group")
    context["form"] = form

    return render(request,"group/create_group.html",context)


# def group_detail(request):
#     context = {}

#     return render(request, "group/group_details.html",context)


class GroupDetailView(DetailView):
    model = MeetAppGroup
