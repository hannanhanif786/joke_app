from django.db import models
from django.contrib.auth.models import User


class Joke(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    setup = models.CharField(max_length=100)
    punctuation = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.user.username + " " + self.setup
