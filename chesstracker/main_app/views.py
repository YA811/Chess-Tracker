# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')

class Game:
    def __init__(self, opponent_name, breed, description, age):
        self.name = opponent_name
        self.date = date
        self.result = result
        self.note = note

def game_index(request):
    cats = Cat.objects.filter(user=request.user)
    return render(request, 'game/index.html', {'game': game})
