from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Topics(models.Model):
    
    topic_name = models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.topic_name

class MeetAppGroup(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    location = models.CharField(max_length=255)
    topics = models.ManyToManyField(Topics)
    desc = models.TextField(max_length=1000,null=False,blank=False,help_text="Enter your group descriptions here...")
    organizer_name = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def truncatecharsStart(self):
        if len(self.desc) > 20:
            char1 = self.desc[:100]
        return char1
    
    def truncatecharsEnd(self):
        char2 = self.desc[100:]
        return char2
    

# class Organizer(models.Model):
#     organizer_name = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="organizer")
#     group_name = models.ManyToManyField(MeetAppGroup)


#     def __str__(self):
#         return self.organizer_name.username


# Signals to create/update User once Instance is created/updated.
# @receiver(post_save, sender=User)
# def create_group(sender, instance, created, **kwargs):
#     if created:
#         Organizer.objects.create(organizer_name=instance)

# @receiver(post_save, sender=User)
# def save_group(sender, instance, **kwargs):
#     instance.name.save()
    