from django.db import models
from django.contrib.auth.models import User



class MyOpsUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    first_name = models.CharField(max_length=25)
    username = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)