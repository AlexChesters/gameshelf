from django.urls import path
from django.shortcuts import redirect

from .views import waiting_to_play_games, currently_playing_games, completed_games, add_a_game, edit_a_game

app_name = "shelf"
urlpatterns = [
    path("", lambda _: redirect("/shelf/playing", permanent=False)),
    path("waiting", waiting_to_play_games, name="waiting"),
    path("playing", currently_playing_games, name="playing"),
    path("completed", completed_games, name="completed"),
    path("add", add_a_game, name="add_a_game"),
    path("edit/<str:game_id>", edit_a_game, name="edit_a_game")
]
