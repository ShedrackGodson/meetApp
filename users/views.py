from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from social_django.models import UserSocialAuth
from django.contrib.auth.models import User, auth
import re
import json
from urllib.request import urlopen
from .models import Profile


def locationTracer():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']


# def register(request):
#     context = {}
#     if request.method=="POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = UserCreationForm()
#     context['form'] = form
#     return render(request,'users/registration.html',context)


def signup(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password"]
        password2 = request.POST["password1"]

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists.")
                return redirect("signup")
            else:
                user = User.objects.create_user(username=username,password=password1)
                user.save()
                auth.authenticate(username=username,password=password1)
                return redirect("/")
        else:
            messages.error(request, "Passwords must match.")
            return redirect("signup")
    else:
        return render(request, "signup.html",context)


def login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Username and/or password are invalid.")
            return redirect("login")
    else:
        return render(request,'login.html',{})


def logout(request):
    auth.logout(request)
    return redirect("/")


@login_required
def settings(request):
    user = request.user

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'index.html', {
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'users/password.html', {'form': form})


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == "facebook":
        Profile.objects.create(
            user=user, 
            photo_url=response['user']['picture']
        )