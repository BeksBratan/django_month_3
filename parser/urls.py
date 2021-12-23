from django.urls import path
from . import views

urlpatterns = [
    path('game/', views.GameView.as_view()),
    path('parser/', views.ParserGameView.as_view()),

]