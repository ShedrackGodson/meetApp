from django.shortcuts import render

def home(request):
    context = {}
    url = "home"
    context['url'] = url
    return render(request,"index.html", context)
