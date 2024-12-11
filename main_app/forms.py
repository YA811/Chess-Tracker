from django import forms
from .models import Game, TrainingSession

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['opponent', 'time_control', 'result', 'pgn']

class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['activity_type', 'duration', 'rating']