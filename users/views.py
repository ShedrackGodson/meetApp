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
from .models import Profile, Interest
from django.shortcuts import get_list_or_404,get_object_or_404
from django.forms.models import model_to_dict
from .form import UserUpdateForm,ProfileUpdateForm


def locationTracer():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    city = data['city']
    country=data['country']
    return city+","+country


def signup(request):
    context = {}
    url = "signup"
    context["url"] = url
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password"]
        password2 = request.POST["password1"]

        if password1==password2:
            if User.objects.filter(username=username).exists():
                user_exists = messages.info(request, "Username already exists.")
                return redirect("signup")
            else:
                user = User.objects.create_user(username=username,password=password1)
                user.save()
                # Automatic login
                return redirect("login")
        else:
            messages.error(request, "Passwords must match.")
            return redirect("signup")
        context["user_exists"] = user_exists
    else:
        return render(request, "signup.html",context)


def login(request):
    context = {}
    url = "login"
    context["url"] = url
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
        return render(request,'login.html',context)


def logout(request):
    auth.logout(request)
    return redirect("/")


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == "facebook":
        Profile.objects.create(
            user=user, 
            photo_url=response['user']['picture']
        )
    elif backend.name == "twitter":
        Profile.objects.create(
            user=user,
            photo_url=response["user"]["picture"]
        )

@login_required
def profile(request):
    context = {}
    url = "profile"
    context["url"] = url

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

    # user_interests = Profile.objects.get(user=user)
    # user_interests.interests.all()
    user_profile = Profile.objects.all()
    # requested user location
    # location = locationTracer()

    prfl = model_to_dict(request.user.profile)
    

    context['twitter_login'] = twitter_login
    context['facebook_login'] = facebook_login
    context['can_disconnect'] = can_disconnect
    context['user_profile'] = user_profile
    # context['location'] = location
    context['user'] = request.user
    

    return render(request, 'users/profile.html', context)

@login_required
def profile_edit(request):
    context = {}

    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context["u_form"] = u_form
    context["p_form"] = p_form

    all_interests = Interest.objects.all()
    context["all_interests"] = all_interests

    return render(request,"users/updateprofil.html",context)