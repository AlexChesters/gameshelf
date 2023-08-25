from django.urls import path

from .views import index, add_a_game, edit_a_game

app_name = "shelf"
urlpatterns = [
    path("", index, name="index"),
    path("add", add_a_game, name="add_a_game"),
    path("edit/<str:game_id>", edit_a_game, name="edit_a_game")
]
