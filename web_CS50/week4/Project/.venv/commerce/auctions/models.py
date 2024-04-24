from django.contrib.auth.models import AbstractUser
from djmoney.models.fields import MoneyField
from django.db import models
from django.utils import timezone
from djmoney.models.validators import MinMoneyValidator
import datetime


class User(AbstractUser):
    pass


class Main_Category(models.Model):
    id = models.AutoField(primary_key=True)
    main_category = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Main_Categories"


class Sub_category(models.Model):
    id = models.AutoField(primary_key=True)
    parent_category = models.ForeignKey(
        Main_Category, on_delete=models.CASCADE, related_name="parent"
    )
    sub_category = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Sub_categories"

    def __str__(self):
        return f"Parent Category: {self.parent_category}, Category: {self.sub_category}"


class Lot(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    title = models.CharField(max_length=50)
    decription = models.TextField(max_length=300)
    starting_price = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency="USD",
    )
    category = models.ForeignKey(
        Sub_category,
        models.CASCADE,
        related_name="category",
    )
    open_time = models.TimeField(default=timezone.now)
    close_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"Lot: {self.title}, Starting Price: {self.starting_price}, Category: {self.category}"


class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name="lot_info")
    bid = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency="USD",
        blank=False,
        validators=[MinMoneyValidator(lot)],
    )
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field="username", related_name="author"
    )
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name="comments")
    post_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=200)
