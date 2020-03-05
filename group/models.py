from django.db import models

class Topics(models.Model):
    topic_name = models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.topic_name
    
