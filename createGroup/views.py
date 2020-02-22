from django.shortcuts import render
from .forms import GroupForm

def groupCreate(request):
    context = {}
    form = GroupForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        organizer = request.user
        obj.organizers.set(organizer)
        obj.save()
        form = GroupForm()
    context['form'] = form
    return render(request,'index.html',context)
