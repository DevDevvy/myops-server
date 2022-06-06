from django.db import models
from django.contrib.auth.models import User


class MyOpsUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    user_photo = models.ImageField(
        upload_to='userphotos', height_field=None,
        width_field=None, max_length=None, null=True)