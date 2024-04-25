from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.forms import DateInput, ModelForm
from auctions.models import Lot, Sub_category, Main_Category
from django import forms
import datetime

from .models import User


class LotForm(ModelForm):
    """Form definition for Lot."""

    class Meta:
        """Meta definition for Lotform."""

        model = Lot
        fields = ("title", "decription", "starting_price", "category", "close_time")
        widgets = {
            "close_time": DateInput(
                attrs={
                    "type": "date",
                    "min": datetime.date.today(),
                    "max": datetime.date.today() + datetime.timedelta(days=60),
                }
            )
        }


def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "auctions/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "auctions/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required()
def add_lot(request):
    if request.method == "POST":
        submited_form = LotForm(request.POST)
        if submited_form.is_valid():
            lot = submited_form.save(commit=False)
            lot.owner = request.user
            lot.open_time = datetime.date.today()
            lot.save()
            submited_form.save

    return render(request, "auctions/add_lot.html", {"form": LotForm()})


def main_categories(request):
    categories = Main_Category.objects.all()
    for category in categories:
        print(category)
    return render(request, "auctions/categories.html", {"categories": categories})


def sub_categories(request, main_category):
    parent = Main_Category.objects.filter(main_category=main_category)
    parent_id = parent[0].id
    sub_categories = Sub_category.objects.filter(parent_category=parent_id)
    for category in sub_categories:
        print(category)
    return render(
        request,
        "auctions/sub_categories.html",
        {"sub_categories": sub_categories, "main_category": main_category},
    )


def category_lot_list(request, main_category, sub_category):
    current_sub_category = Sub_category.objects.get(sub_category=sub_category)
    sub_category_id = current_sub_category.id
    lots = Lot.objects.filter(category=sub_category_id)
    return render(
        request,
        "auctions/category_lots.html",
        {
            "lots": lots,
            "current_category": sub_category,
            "main_category": main_category,
        },
    )


def lot_page(request, lot_id):
    lot = Lot.objects.get(pk=lot_id)
    lot_sub_category = lot.category
    lot_main_category = lot_sub_category.parent_category
    link = f"/auctions/{lot_main_category}/{lot_sub_category}/{lot_id}"
    render(request, link, {"lot": lot})
