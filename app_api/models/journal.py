from django.db import models

class Journal(models.Model):
    content = models.CharField(max_length=500)
    title = models.CharField(max_length=40)
    user = models.ForeignKey("MyOpsUser", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    mood = models.ForeignKey("Mood", on_delete=models.CASCADE)