from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add_lot", views.add_lot, name="add_lot"),
    path("categories/", views.main_categories, name="main_categories"),
    path(
        "categories/<str:main_category>/",
        views.sub_categories,
        name="sub_categories",
    ),
    path(
        "categories/<str:main_category>/<str:sub_category>",
        views.category_lot_list,
        name="category_lot_list",
    ),
    path(
        "categories/<str:main_category>/<str:sub_category>/<int:lot_id>",
        views.lot_page,
        name="lot_page",
    ),
    path("close_lot/<int:lot_id>", views.close_lot, name="close_lot"),
    path(
        "place_bid//<str:main_category>/<str:sub_category>/<int:lot_id>",
        views.place_bid,
        name="place_bid",
    ),
    path(
        "update-bid-info/<int:lot_id>/", views.update_bid_info, name="update_bid_info"
    ),
    path(
        "add_comment/<int:lot_id>/<int:user_id>/",
        views.add_comment,
        name="add_comment",
    ),
    path("wishlist/<int:lot_id>/<int:user_id>/", views.wishlist, name="wishlist"),
    path("user_wishlist/", views.user_wishlist, name="user_wishlist"),
]
