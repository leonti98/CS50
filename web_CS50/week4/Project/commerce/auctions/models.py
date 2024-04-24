from django.contrib.auth.models import AbstractUser
from django.fields 
from django.db import models


class User(AbstractUser):
    pass


class Product(models.Model):
    title - models.CharField(max_length=20)
    description = models.TextField(max_length=400)
    models.ImageField(
        _(""), upload_to=None, height_field=None, width_field=None, max_length=None
    )
    sratring_price = models.DecimalField(max_digits=6, decimal_places=2)
    sratring_price = models.
