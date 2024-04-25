from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.forms import DateInput, ModelForm
from auctions.models import Lot
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


@login_required(redirect_field_name="/login")
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
