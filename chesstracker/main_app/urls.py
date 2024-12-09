from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('game/', views.add_game, name='add_game'),
    path('your-games/', views.game_list, name='your_games'),
    path('training-session/', views.add_training_session, name='add_training_session'),
]