from django.db import models
from users.models import Profile
from django.contrib.auth.models import User


class Topics(models.Model):
    topic_name = models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.topic_name

class Group(models.Model):
    CITY_CHOICES = (
        ("Male","Male"),
        ("Female","Female"),
        ("Not Interested","Not Interested")
    )
    name = models.CharField(max_length=255,null=False,blank=False)
    group_location = models.CharField(max_length=255,choices=CITY_CHOICES)
    group_topics = models.ManyToManyField(Topics)
    group_desc = models.TextField(max_length=1000,null=False,blank=False)

    def __str__(self):
        return self.name
    
