from django.db import models
from accounts.models import User

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Likes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts,on_delete=models.CASCADE)

class HashTags(models.Model):
    tagname = models.CharField(max_length=30, unique=True)

class PostTags(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)