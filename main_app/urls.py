from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('game/new/', views.add_game, name='add_game'),
    path('your-games/', views.game_list, name='your_games'),
    path('training-session/new/', views.add_training_session, name='add_training_session'),
    path('training-sessions/', views.training_sessions, name='training_sessions'), 
    path('game/<int:game_id>/', views.game_details, name='game_details'),
    path('training_session/<int:session_id>/', views.training_session_detail, name='training_session_detail'),
    path('training_session/<int:session_id>/delete/', views.delete_training_session, name='delete_training_session'),
    path('game/<int:game_id>/delete/', views.delete_game, name='delete_game'),
    path('training_session/<int:session_id>/update/', views.update_training_session, name='update_training_session'),
    path('game/<int:game_id>/update/', views.update_game, name='update_game'),
    path('accounts/signup/', views.signup, name='signup'),
]