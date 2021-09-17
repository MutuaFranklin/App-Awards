from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = CloudinaryField('Profile Pic')
    bio =  models.TextField(blank=True, default='Welcome to my world')
    location = models.CharField(max_length = 50,blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 

    def edit_bio(self, new_bio):
        self.bio = new_bio
        self.save()