from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('game/new/', views.add_game, name='add_game'),
    path('your-games/', views.game_list, name='your_games'),
    path('training-session/', views.add_training_session, name='add_training_session'),
    path('training-sessions/', views.training_sessions, name='training_sessions'), 
]