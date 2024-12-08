from django.db import models
from django.contrib.auth.models import User

class TrainingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_date = models.DateField(auto_now_add=True)
    activity_type = models.CharField(max_length=50, choices=[('game', 'Game')])
    duration = models.IntegerField()  # Duration of the session in minutes
    rating = models.IntegerField(default=0)  # Rating change from the session

# Game model
class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
    game_date = models.DateField(auto_now_add=True)
    opponent = models.CharField(max_length=100)
    time_control = models.CharField(max_length=50, choices=[('blitz', 'Blitz'), ('rapid', 'Rapid'), ('classical', 'Classical')])
    result = models.CharField(max_length=10, choices=[('win', 'Win'), ('loss', 'Loss'), ('draw', 'Draw')])
    pgn = models.TextField()  # PGN of the game for review
