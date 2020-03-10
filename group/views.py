from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.views import locationTracer
from users.models import Interest
from .models import Topics, MeetAppGroup
import random
from .forms import GroupCreationForm


@login_required
def groups(request):
    context = {
        
    }
    # location = locationTracer()
    # context["location"] = location
    group_topics = Topics.objects.all()[0:23]
    context["topics"] = group_topics
    form = GroupCreationForm(request.POST)
    if request.method=="POST":
        # name = request.POST["group_name"]
        # location = request.POST["location"]
        # desc = request.POST["group_desc"]
        # topics = request.POST["group_topic"]
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Group Created.")
            return redirect("/")
        else:
            form = GroupCreationForm(request.POST)
            print("Group not created.")
            return redirect("group")

        """Checking if the group exists, If YES then disallow the creation of duplicates"""
        # if MeetAppGroup.objects.filter(name=name).exists():
        #     print("Group attempted to create already exists,Find another name and try again.")
        #     return redirect("group")
        # else:
        #     groupID = random.randint(1,100000000)
        #     group = MeetAppGroup(groupID,name,location,topics,desc)
        #     group.save()
        #     print("Group created succesfully.")
        #     return redirect("group")
    context["form"] = form
    return render(request,"group/create_group.html",context)
