from django.db import models
from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default="Hello there!")
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
        
    def __str__(self):
        return f'{self.user} Profile'
        

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()        

