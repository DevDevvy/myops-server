from django.db import models
from django.contrib.auth.models import User


class Mood(models.Model):
    mood = models.CharField(max_length=20)
