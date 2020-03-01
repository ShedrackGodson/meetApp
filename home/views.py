from django.shortcuts import render,redirect
from social_django.models import UserSocialAuth
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from users.models import Profile,Interest
from django.forms.models import model_to_dict
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


@login_required
def home(request):
    context = {}
    url = "home"
    context['url'] = url
    user = request.user

    context["user"] = request.user

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    context["twitter_login"] = twitter_login
    context["facebook_login"] = facebook_login
    context["can_disconnect"] = can_disconnect

    return render(request, 'index.html', context)


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