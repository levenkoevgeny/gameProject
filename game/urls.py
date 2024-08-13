from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('', views.game_list, name='game-list'),
    path('<game_id>/start', views.new_game_start_page, name='new-game-start-page'),
    path('running', views.game_running, name='game-running'),
    path('results', views.game_results, name='game-results'),
    path('game-over', views.game_over, name='game-over'),
]