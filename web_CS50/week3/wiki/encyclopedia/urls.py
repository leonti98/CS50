from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("suggestions", views.suggestions, name="suggetions"),
    path("add_page", views.add_page, name="add_page"),
    path("wiki/random_page", views.random_page, name="random_page"),
    path("wiki/<str:entry_title>", views.entry_page, name="entry_page"),
    path("edit/<str:entry_title>", views.edit_page, name="edit_page"),
]
