from django.shortcuts import render


def home(request):
    """
    Pantalla principal (landing) de Figures That Teach / Figuras que enseñan.
    Muestra la portada basada en el diseño de MainPage.png.
    """
    return render(request, "game/home.html")


def game_view(request):
    """
    Pantalla de juego donde se muestra la cámara del niño y las figuras interactivas.
    """
    return render(request, "game/game.html")

def end_view(request):
    """
    Pantalla final del juego
    """
    return render(request, "game/end.html")


