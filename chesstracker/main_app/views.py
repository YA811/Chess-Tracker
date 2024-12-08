# main_app/views.py

# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Game, TrainingSession
from .forms import GameForm, TrainingSessionForm


# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.user = request.user
            game.save()
            return redirect('home')
    else:
        form = GameForm()
    return render(request, 'add_game.html', {'form': form})


def add_training_session(request):
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect('home')
    else:
        form = TrainingSessionForm()
    return render(request, 'add_training_session.html', {'form': form})

