import profile

from django.urls import path
from user.views.authentication_view import register, login_user, logout_user
from user.views.joke_view import joke_view, create_joke

urlpatterns = [
    path('register', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', joke_view, name='joke_view'),
    path('create_joke', create_joke, name='create_joke')
]