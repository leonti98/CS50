from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("levan", views.levan, name="levan"),
    path("david", views.david, name="david"),
]