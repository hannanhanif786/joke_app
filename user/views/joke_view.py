import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.models import Joke
from user.tasks import create_joke_file

@login_required(login_url="login")
def joke_view(request):
    jokes = Joke.objects.filter(user=request.user)
    return render(request, 'joke.html', {'jokes': jokes})


@login_required(login_url="login")
def create_joke(request):
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    if response.status_code == 200:
        joke = response.json()
        Joke.objects.create(user=request.user, setup=joke['setup'], punctuation=joke['punchline'])
    return redirect('/')


@login_required(login_url="login")
def create_file(request):
    user = request.user
    create_joke_file.delay(user.id)
    return redirect("/")

