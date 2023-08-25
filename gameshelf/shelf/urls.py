from django.urls import path

from .views import index, add_a_game

app_name = "shelf"
urlpatterns = [
    path("", index, name="index"),
    path("add", add_a_game, name="add_a_game")
]
