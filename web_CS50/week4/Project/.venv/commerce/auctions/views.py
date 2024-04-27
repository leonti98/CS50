from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.forms import DateInput, ModelForm
from auctions.models import Lot, Sub_category, Main_Category, Bid
from django import forms
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator
from django.contrib import messages
import datetime

from .models import User


class LotForm(ModelForm):
    """Form to add new lots"""

    class Meta:

        model = Lot
        fields = (
            "title",
            "description",
            "starting_price",
            "category",
            "close_time",
            "image",
        )
        widgets = {
            "close_time": DateInput(
                attrs={
                    "type": "date",
                    "min": datetime.date.today(),
                    "max": datetime.date.today() + datetime.timedelta(days=60),
                }
            )
        }


class CloseForm(forms.Form):
    """From to close Lots."""

    lot_id = forms.HiddenInput()


# class BidForm(forms.Form):
#     amount = MoneyField


class BidForm(forms.ModelForm):
    """Form definition for Bid."""

    class Meta:
        """Meta definition for Bidform."""

        model = Bid
        fields = ("bid",)  # Notice the comma after "bid"


def index(request):
    lots = Lot.objects.all()
    return render(request, "auctions/index.html", {"lots": lots})


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
        form = LotForm(request.POST)
        if form.is_valid():
            lot = form.save(commit=False)
            lot.owner = request.user
            lot.open_time = datetime.date.today()
            lot.save()

    return render(request, "auctions/add_lot.html", {"form": LotForm()})


def main_categories(request):
    categories = Main_Category.objects.all()
    return render(request, "auctions/categories.html", {"categories": categories})


def sub_categories(request, main_category):
    parent = Main_Category.objects.filter(main_category=main_category)
    parent_id = parent[0].id
    sub_categories = Sub_category.objects.filter(parent_category=parent_id)
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


def lot_page(request, main_category, sub_category, lot_id):
    if request.method == "POST":
        submited_from = BidForm(request.POST)
        if submited_from.is_valid():
            lot = Lot.objects.get(pk=lot_id)
            bid = submited_from.save(commit=False)
            money = submited_from.cleaned_data["bid"]
            if money.amount > lot.starting_price.amount:
                if lot.highest_bid is None or lot.highest_bid.amount < money.amount:
                    bid.lot = lot
                    bid.bidder = request.user
                    bid.save()
                    message = "Bid was succesfully placed"
                else:
                    message = "Your bid was lower than highest bid"

            else:
                message = "Your bid was lower than starting price"
    lot = Lot.objects.get(pk=lot_id)
    try:
        if message:
            pass
    except:
        if lot.highest_bidder == request.user:
            message = None
        else:
            message = None
    return render(
        request,
        "auctions/single_lot.html",
        {
            "lot": lot,
            "main_category": main_category,
            "sub_category": sub_category,
            "bid_form": BidForm,
            "close_form": CloseForm,
            "highest_bid": lot.highest_bid,
            "highest_bidder": lot.highest_bidder,
            "message": message,
        },
    )


def close_lot(request, lot_id):
    if request.method == "POST":
        lot = Lot.objects.get(pk=lot_id)
        lot.is_open = False
        lot.save()
    return HttpResponseRedirect("/")


def place_bid(request, lot_id):
    if request.method == "POST":
        bid_form = BidForm
        pass
    return HttpResponseRedirect("/")


def update_bid_info(request, lot_id):
    try:
        lot = Lot.objects.get(pk=lot_id)
        if lot.highest_bidder != request.user:
            message = "You are no longer highest bidder. Refresh page"
            alert_class = "alert alert-warning role=alert"
        else:
            message = "You are still Highest bidder"  # You can add additional messages here if needed
            alert_class = "alert alert-success role=alert"
        context = {"message": message, "alert_class": alert_class}
        return JsonResponse(context)

    except Lot.DoesNotExist:
        return JsonResponse({"error": "Lot not found"}, status=404)
