from django.db import models

class Favorite(models.Model):
    tip = models.ForeignKey("tip", on_delete=models.CASCADE)
    user = models.ForeignKey("MyOpsUser", on_delete=models.CASCADE)