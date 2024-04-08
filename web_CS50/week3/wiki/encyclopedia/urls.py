from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_title>", views.entry_page, name="entry_page"),
    path("search", views.search, name="search"),
    path("suggestions", views.suggestions, name="suggetions"),
    path("add_page", views.add_page, name="add_page")
]
