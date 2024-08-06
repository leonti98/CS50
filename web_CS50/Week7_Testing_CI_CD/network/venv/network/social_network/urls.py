from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"soucial_network", views.BlogPostViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("blogposts/", views.BlogPostListCreate.as_view(), name="create_post"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path(
        "blogposts/<int:pk>/",
        views.BlogPostRetrieveUpdateDestroy.as_view(),
        name="update",
    ),
    path("blogposts/list", views.BlogPostList.as_view(), name="blogpostslists"),
    path("get_posts", views.get_posts, name="get_posts"),
    path("api/", include(router.urls)),
]
