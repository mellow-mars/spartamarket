from django.db import models
from accounts.models import User


class Posts(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank = True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(User,related_name='like_posts')


class HashTags(models.Model):
    tagname = models.CharField(max_length=30, unique=True)


class PostTags(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


