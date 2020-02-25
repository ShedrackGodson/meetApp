from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Interest(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True,help_text="A valid email address")
    location = models.CharField(max_length=255)
    hometown = models.CharField(max_length=255)
    bio = models.TextField(max_length=500, blank=True)
    interests = models.ManyToManyField(Interest, related_name="interests")
    avatar = models.ImageField(verbose_name="Profile Image")
    birthdate = models.DateField(null=True, blank=True)

    # def __str__(self):
    #     return self.email
    def __repr__(self):
      return super().__repr__() + "Email: " + str(self._email) 
    


# Signals to create/update once User Instance is created/updated.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
