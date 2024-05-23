from django.contrib import admin
from .models import Main_Category, Sub_category, Lot, Bid, Comment, Wishlist


# Register your models here.
admin.site.register(Main_Category)
admin.site.register(Sub_category)
admin.site.register(Lot)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Wishlist)
