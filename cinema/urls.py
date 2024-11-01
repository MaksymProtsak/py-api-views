from django.urls import path

from cinema.views import (
    genre_list,
    genre_detail,
    movie_list,
    movie_detail
)

urlpatterns = [
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre-detail"),
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"
