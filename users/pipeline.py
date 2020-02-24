from .models import Profile

def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == "facebook":
        Profile.objects.create(
            user=user, 
            photo_url=response['user']['picture']
        )
        user.save()