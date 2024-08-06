from rest_framework import serializers
from .models import BlogPost, Comment, User


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        managed = True
        verbose_name = "BlogPost"
        verbose_name_plural = "BlogPosts"
        fields = "__all__"
