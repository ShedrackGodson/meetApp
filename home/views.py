from django.shortcuts import render
from social_django.models import UserSocialAuth
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required




def home(request):
    context = {}
    url = "home"
    context['url'] = url
    # user = request.user

    # try:
    #     twitter_login = user.social_auth.get(provider='twitter')
    # except UserSocialAuth.DoesNotExist:
    #     twitter_login = None

    # try:
    #     facebook_login = user.social_auth.get(provider='facebook')
    # except UserSocialAuth.DoesNotExist:
    #     facebook_login = None

    # can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
    # context['twitter_login'] = twitter_login
    # context['facebook_login'] = facebook_login
    # context['can_disconnect'] = can_disconnect

    return render(request, 'index.html', context)


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