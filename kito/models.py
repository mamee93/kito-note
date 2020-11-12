from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone
# Create your models here.

class Header(models.Model):
    
    userheader  = models.ForeignKey(User, related_name='userheader', on_delete=models.CASCADE,blank=True,null=True  )
    title       = models.CharField(max_length=100)
    content     = models.TextField(max_length=1000)
    image       = models.ImageField(upload_to='header/')
    created_at  = models.DateTimeField(auto_now=True) 
    update_at   = models.DateTimeField(auto_now_add=True)
    post_slug   = models.SlugField(blank=True, null=True)
     
    
    def save(self, *args, **kwargs):

        self.post_slug = self.title
        super(Header,self).save(*args, **kwargs)
        
    def __str__(self):

        return self.title

class Kito(models.Model):
    
    owner  = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE,blank=True,null=True  )
    title       = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now=True) 
    post_slug   = models.SlugField(blank=True, null=True)
    update_at   = models.DateTimeField(auto_now_add=True)
    img       = models.ImageField(upload_to='kito/')
    content     = models.TextField(max_length=1000)
    Kg          = models.IntegerField(default=1)
    day         = models.IntegerField(default=1)

    @property
    def get_photo_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url
        else:
            return "/static/img/1.jpg"
    def save(self, *args, **kwargs):

        self.post_slug = self.title
        super(Kito,self).save(*args, **kwargs)
        
    def __str__(self):

        return self.title

class Comments(models.Model):
    user        = models.ForeignKey(User, related_name='userComment', on_delete=models.CASCADE,blank=True,null=True  )
    Kito       = models.ForeignKey('Kito', related_name='Comments_kito', on_delete=models.CASCADE  )
    comments    = models.TextField(blank=True, null=True)
    created_at  = models.DateTimeField(default=timezone.now)
    update_at   = models.DateTimeField(auto_now_add=True)




class SameEat(models.Model):
    
    user             = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE  )
    title            = models.CharField(max_length=100)
    created_at       = models.DateTimeField(auto_now=True) 
    post_slug        = models.SlugField(blank=True, null=True)
    update_at        = models.DateTimeField(auto_now_add=True)
    image            =  models.ImageField(upload_to='cook/')
    content          = models.TextField(max_length=1000)
    
   
    
    def save(self, *args, **kwargs):

        self.post_slug = self.title
        super(SameEat,self).save(*args, **kwargs)
        
    def __str__(self):

        return self.title