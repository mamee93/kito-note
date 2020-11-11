from django.db import models
from  django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class  Profile(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/')
    bio   = models.TextField(blank=True,max_length=250)
    def __str__(self):
        return self.user.username
    
    
 
        return "/static/images/user.jpg"
@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
   