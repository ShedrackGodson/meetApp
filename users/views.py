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
from .form import (
    UserUpdateForm,
    ProfileUpdateForm,
    UserUpdateEmail, 
    UserLocationForm,
    UserBirthdayForm,
    UserGenderUpdateForm,
    UserBioUpdateForm
)


"""
A function to track the site visitors actual location based on their IP addresses. IP address got
passed direct to http://ipinfo.io to check for the current Location and data is returned as json
"""
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

"""
Saving the users profiles who are logging in and signing up with Facebook and/or Twitter
"""
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

    prfl = model_to_dict(request.user.profile)
    

    context['twitter_login'] = twitter_login
    context['facebook_login'] = facebook_login
    context['can_disconnect'] = can_disconnect
    context['user_profile'] = user_profile
    context['user'] = request.user
    

    return render(request, 'users/profile.html', context)

"""
Editing User & Profile fields separately. This may be dumb but for the meantime I am looking for the 
scenario that makes more sense. It works though but I dont think this is the better way of handling
multiple fields separately.
"""
@login_required
def profile_edit(request):
    context = {}
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        e_form = UserUpdateEmail(request.POST, instance=request.user)
        l_form = UserLocationForm(request.POST, instance=request.user.profile)
        b_form = UserBirthdayForm(request.POST, instance=request.user.profile)
        g_form = UserGenderUpdateForm(request.POST, instance=request.user.profile)
        bio_form = UserBioUpdateForm(request.POST, instance=request.user.profile)

        if u_form.is_valid():
            u_form.save()
            print("Profile updated")
            return redirect("setting")
        
        if e_form.is_valid():
            e_form.save()
            print("Email updated.")
            return redirect("setting")
        
        if l_form.is_valid():
            l_form.save()
            print("Location and/or Hometown Updated.")
            return redirect("setting")

        if b_form.is_valid():
            b_form.save()
            print("Birthday Updated.")
            return redirect("setting")

        if g_form.is_valid():
            g_form.save()
            print("Gender Updated.")
            return redirect("setting")
        
        if bio_form.is_valid():
            bio_form.save()
            print("Bio updated.")
            return redirect("setting")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        e_form = UserUpdateEmail(instance=request.user)
        l_form = UserLocationForm(instance=request.user.profile)
        b_form = UserBirthdayForm(instance=request.user.profile)
        g_form = UserGenderUpdateForm(instance=request.user.profile)
        bio_form = UserBioUpdateForm(instance=request.user.profile)

    context["u_form"] = u_form
    context["p_form"] = p_form
    context["e_form"] = e_form
    context["l_form"] = l_form
    context["b_form"] = b_form
    context["g_form"] = g_form
    context["bio_form"] = bio_form

    all_interests = Interest.objects.all()[0:25]
    context["all_interests"] = all_interests

    return render(request,"users/updateprofil.html",context)