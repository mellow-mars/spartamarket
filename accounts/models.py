from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='images/', blank=True)
    date_joined = models.DateTimeField(auto_now=True)


class Follows(models.Model):
    following_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')
    followed_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followed')
