from django.db import models
from geopy.geocoders import Nominatim

def location():
    geolocator = Nominatim(user_agent="https://ba531876.ngrok.io")
    loc = geolocator.geocode("5 Shaaban Robert St, Dar es Salaam")

class Organizer(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    title = models.CharField(max_length=255,null=False)
    location_address = models.CharField(max_length=255,null=False)
    member_since = models.DateTimeField(verbose_name='Account Since', auto_now_add=True,null=False)
    bio = models.CharField(max_length=255)
    profile_picture = models.ImageField(verbose_name='Profile Image',null=False)

    def __str__(self):
        return self.name
    


class GroupDetails(models.Model):
    group_name = models.CharField(max_length=255,null=False)
    group_location = models.CharField(max_length=255,null=False, blank=False)
    total_members = models.IntegerField(default=0)
    organizers = models.ManyToManyField(Organizer)
    group_about = models.CharField(max_length=255,null=False)
    thumbnail = models.ImageField(verbose_name='Group Picture', null=False)

    def __str__(self):
        return self.group_name
    
