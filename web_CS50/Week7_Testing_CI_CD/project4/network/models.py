from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def serialize(self):
        return {}

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField(max_length=500)

    def __str__(self):
        return self.comment_content[:20]
