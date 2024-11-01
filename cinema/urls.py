from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    genre_list,
    genre_detail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieListViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieListViewSet)

urlpatterns = [
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path(
        "cinema_halls/",
        CinemaHallViewSet.as_view(
            actions={
                "get": "list",
                "post": "create",
            }
        ),
        name="cinema_halls-list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallViewSet.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="cinema_halls-detail"
    ),
    path("", include(router.urls))
]

app_name = "cinema"
