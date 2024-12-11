# main_app/views.py

from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from .models import Game, TrainingSession
from .forms import GameForm, TrainingSessionForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
# Add the two imports below
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')

def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})


def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.user = request.user
            session, created = TrainingSession.objects.get_or_create(
                activity_type='game', 
                defaults={'duration': 60, 'rating': 0} 
            )
            game.session = session
            game.save()

            return redirect('your_games')
    else:
        form = GameForm()
    return render(request, 'add_game.html', {'form': form})

def add_training_session(request):
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('training_sessions')
    else:
        form = TrainingSessionForm()
    
    return render(request, 'add_training_session.html', {'form': form})

def training_sessions(request):
    trainings = TrainingSession.objects.all()  
    return render(request, 'training_sessions.html', {'trainings': trainings})

def game_details(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'game_details.html', {'game': game})

def training_session_detail(request, session_id):
    session = get_object_or_404(TrainingSession, id=session_id)
    return render(request, 'training_session_detail.html', {'session': session})

def delete_training_session(request, session_id):
    session = get_object_or_404(TrainingSession, id=session_id)
    if request.method == 'POST':
        session.delete()
        return redirect('training_sessions')
    return HttpResponseNotAllowed(['POST'])

def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        game.delete()
        return redirect('your_games') 
    return HttpResponseNotAllowed(['POST'])

def update_training_session(request, session_id):
    session = get_object_or_404(TrainingSession, id=session_id)
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('training_session_detail', session_id=session.id)
    else:
        form = TrainingSessionForm(instance=session)
    return render(request, 'update_training_session.html', {'form': form, 'session': session})

def update_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game) 
        if form.is_valid():
            form.save()  
            return redirect('game_details', game_id=game.id) 
    else:
        form = GameForm(instance=game) 
    return render(request, 'update_game.html', {'form': form, 'game': game})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('about')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )