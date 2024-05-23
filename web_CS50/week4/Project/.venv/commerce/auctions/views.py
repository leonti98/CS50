from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.forms import DateInput, ModelForm
from auctions.models import Lot, Sub_category, Main_Category, Bid, Comment, Wishlist
from django import forms
from django.contrib import messages
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

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


class WishlistForm(forms.ModelForm):
    """Form definition for Wishlist."""

    class Meta:
        """Meta definition for Wishlistform."""

        model = Wishlist
        fields = {}


class CommentForm(ModelForm):
    """CommentForm definition."""

    class Meta:
        model = Comment
        fields = ("text",)
        labels = {
            "text": "Write a comment",
        }
        widgets = {
            "text": forms.Textarea(
                attrs={"type": "text", "rows": 3, "class": "form-control"}
            )
        }


class CloseForm(forms.Form):
    """From to close Lots."""

    lot_id = forms.HiddenInput()


class BidForm(forms.ModelForm):
    """Form definition for Bid."""

    class Meta:
        """Meta definition for Bidform."""

        model = Bid
        fields = ("bid",)
        labels = {"bid": ""}
        # widgets = {
        #     "text": MoneyWidget(
        #         attrs={"type": "text", "rows": 3, "class": "form-control"}
        #     )
        # }


def index(request):
    lots = Lot.objects.filter(is_open=True).order_by("-open_time")
    p = Paginator(lots, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get("page")
    try:
        lots = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        lots = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        lots = p.page(p.num_pages)
    # sending the page object to index.html
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
    lots = Lot.objects.filter(category=sub_category_id, is_open=True).order_by(
        "-open_time"
    )
    p = Paginator(lots, 5)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get("page")
    try:
        lots = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        lots = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        lots = p.page(p.num_pages)
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
    lot = Lot.objects.get(pk=lot_id)
    if request.method == "POST":
        submited_from = BidForm(request.POST)
        if submited_from.is_valid():
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
    try:
        comments = Comment.objects.filter(lot=lot)
    except:
        comments = None
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
            "comments": comments,
            "comment_form": CommentForm,
        },
    )


@login_required
def close_lot(request, lot_id):
    if request.method == "POST":
        lot = Lot.objects.get(pk=lot_id)
        lot.is_open = False
        lot.save()
        print("wtf!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return redirect(
            "lot_page",
            main_category=lot.category.parent_category,
            sub_category=lot.category,
            lot_id=lot.id,
        )


@login_required
def place_bid(request, main_category, sub_category, lot_id):
    lot = Lot.objects.get(pk=lot_id)
    if request.method == "POST":
        submited_from = BidForm(request.POST)
        if submited_from.is_valid():
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
        else:
            message = "Form was invalid"
    else:
        return HttpResponseRedirect("/")
    try:
        comments = Comment.objects.filter(lot=lot)
    except:
        comments = None

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
            "comments": comments,
            "comment_form": CommentForm,
        },
    )


def update_bid_info(request, lot_id):
    try:
        lot = Lot.objects.get(pk=lot_id)
        if lot.highest_bidder != request.user:
            message = "You are no longer highest bidder. Refresh page"
            alert_class = "alert alert-warning role=alert"
            highest_bid = str(lot.highest_bid)
            highest_bidder = lot.highest_bidder.username
        else:
            message = "You are still Highest bidder"  # You can add additional messages here if needed
            alert_class = "alert alert-success role=alert"
            highest_bid = str(lot.highest_bid)
            highest_bidder = lot.highest_bidder.username
        context = {
            "message": message,
            "alert_class": alert_class,
            "highest_bid": highest_bid,
            "highest_bidder": highest_bidder,
        }
        return JsonResponse(context)
    except Lot.DoesNotExist:
        return JsonResponse({"error": "Lot not found"}, status=404)


@login_required
def add_comment(request, lot_id, user_id):
    if request.method == "POST":
        lot = Lot.objects.get(pk=lot_id)
        user = User.objects.get(pk=user_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = user
            comment.lot = lot
            comment.save()
            try:
                comments = Comment.objects.filter(lot=lot)
            except:
                comments = None
        return render(
            request,
            "auctions/single_lot.html",
            {
                "lot": lot,
                "main_category": lot.category.parent_category,
                "sub_category": lot.category,
                "bid_form": BidForm,
                "close_form": CloseForm,
                "highest_bid": lot.highest_bid,
                "highest_bidder": lot.highest_bidder,
                "message": None,
                "comments": comments,
                "comment_form": CommentForm,
            },
        )


@login_required
def wishlist(request, lot_id, user_id):
    if request.method == "POST":
        lot = Lot.objects.get(pk=lot_id)
        user = User.objects.get(pk=user_id)
        form = WishlistForm(request.POST)
        form.user = user
        form.lot = lot
        if form.is_valid():
            user_wishes = user.wished_lots.all()
            for item in user_wishes:
                if str(lot_id) == str(item):
                    query = Wishlist.objects.filter(lot=lot)
                    if query:
                        query.delete()
                        context = {
                            "bookmark_message": "removed bookmark from wishlist",
                            "bookmark_attr": "btn btn-outline-danger",
                        }
                        return JsonResponse(context)
            wish = form.save(commit=False)
            wish.user = user
            wish.lot = lot
            wish.save()
            context = {
                "bookmark_message": "Added to wishlist",
                "bookmark_attr": "btn btn-outline-success",
            }
            return JsonResponse(context)


@login_required
def user_wishlist(request):
    user = request.user
    wished_items = Wishlist.objects.filter(user=user)
    open_lots = []
    closed_lots = []
    if wished_items:
        for item in wished_items:
            if item.lot.is_open:
                open_lots.append(item.lot)
            else:
                closed_lots.append(item.lot)
    return render(
        request,
        "auctions/wishlist.html",
        {"open_lots": open_lots, "closed_lots": closed_lots},
    )


@login_required
def user_listings(request):
    user = request.user
    open_lots = Lot.objects.filter(owner=user, is_open=True)
    closed_lots = Lot.objects.filter(owner=user, is_open=False)
    return render(
        request,
        "auctions/user_listings.html",
        {"open_lots": open_lots, "closed_lots": closed_lots},
    )
