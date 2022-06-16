from django.db import models


class Tip(models.Model):
    tip = models.CharField(max_length=50)
    mood = models.ForeignKey("Mood", on_delete=models.CASCADE)
    user = models.ForeignKey("MyOpsUser", on_delete=models.CASCADE)
    favorites = models.ManyToManyField("MyOpsUser", through="favorite", related_name='favoritedtips')
    public = models.BooleanField()