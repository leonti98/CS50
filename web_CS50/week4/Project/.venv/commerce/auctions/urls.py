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
]
