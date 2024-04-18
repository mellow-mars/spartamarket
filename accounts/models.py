from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='images/', blank=True)
    date_joined = models.DateTimeField(auto_now=True)
    followings = models.ManyToManyField('self',symmetrical=False, related_name='followers')


