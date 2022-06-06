from django.db import models
from django.contrib.auth.models import User


class Tip(models.Model):
    tip = models.CharField(max_length=50)
    mood = models.ForeignKey("Mood", on_delete=models.CASCADE)
    user = models.ForeignKey("MyOpsUser", on_delete=models.CASCADE)
