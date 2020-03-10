from django.db import models
from users.models import Profile
from django.contrib.auth.models import User
from users.views import locationTracer


# location = locationTracer()

class Topics(models.Model):
    
    topic_name = models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.topic_name

class MeetAppGroup(models.Model):
    CITY_CHOICES = (
        ("Tanzania","TZ"),
        ("Uganda","UG"),
        ("Kenya","KN"),
        ("Nigeria","NG"),
        ("South Africa","RSA"),
        ("India","IND"),
    )
    name = models.CharField(max_length=255,null=False,blank=False)
    location = models.CharField(max_length=255)
    topics = models.ManyToManyField(Topics)
    desc = models.TextField(max_length=1000,null=False,blank=False,help_text="Enter your group descriptions here...")

    def __str__(self):
        return self.name
    
