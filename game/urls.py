from django.urls import path

from . import views

app_name = "game"

urlpatterns = [
    # Portada principal
    path("", views.home, name="home"),
    # Pantalla de juego
    path("game/", views.game_view, name="game"),
]


