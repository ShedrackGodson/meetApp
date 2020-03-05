from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.views import locationTracer
from .models import Topics


@login_required
def groups(request):
    context = {
        
    }
    # location = locationTracer()
    # context["location"] = location
    topics = Topics.objects.all()[0:23]
    context["topics"] = topics

    return render(request,"group/create_group.html",context)
