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

    def __str__(self):
        return self.main_category


class Sub_category(models.Model):
    id = models.AutoField(primary_key=True)
    parent_category = models.ForeignKey(
        Main_Category, on_delete=models.CASCADE, related_name="parent"
    )
    sub_category = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Sub_categories"

    def __str__(self):
        return self.sub_category


class Lot(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    title = models.CharField(max_length=50)
    decription = models.TextField(max_length=3000)
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
    open_time = models.DateField(default=datetime.date.today)
    close_time = models.DateField(
        verbose_name="Lot Closing Date", default=datetime.date.today
    )
    image = models.URLField(
        ("Please insert link to image"), max_length=2000, default=None
    )
    is_open = models.BooleanField(default=True)

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

    def __str__(self):
        return self.bid


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field="username", related_name="author"
    )
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name="comments")
    post_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.text


class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
    )
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name="lot")

    def __str__(self):
        return self.lot.title
