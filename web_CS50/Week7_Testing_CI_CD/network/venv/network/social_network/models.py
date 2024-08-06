from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings


class User(AbstractUser):
    followers = models.ManyToManyField(
        "self", blank=True, related_name="user_followers", symmetrical=False
    )
    following = models.ManyToManyField(
        "self", blank=True, related_name="user_following", symmetrical=False
    )
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=10000)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-post_date"]


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="comments"
    )
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.author.username}: {self.comment_content[:20]}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["-comment_time"]
