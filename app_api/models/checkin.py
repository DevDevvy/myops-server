from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CheckIn(models.Model):

    user = models.ForeignKey("MyOpsUser", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    mood_score = models.IntegerField(default=0,validators=[MaxValueValidator(10),MinValueValidator(0)])
    self_talk = models.IntegerField(default=0,validators=[MaxValueValidator(10),MinValueValidator(0)])
    sleep_quality = models.IntegerField(default=0,validators=[MaxValueValidator(10),MinValueValidator(0)])
    coping_strategies = models.IntegerField(default=0,validators=[MaxValueValidator(10),MinValueValidator(0)])
    productivity = models.IntegerField(default=0,validators=[MaxValueValidator(10),MinValueValidator(0)])
    work_time = models.FloatField(default=0,validators=[MaxValueValidator(24),MinValueValidator(0)])
    break_time = models.FloatField(default=0,validators=[MaxValueValidator(24),MinValueValidator(0)])
    personal_time = models.FloatField(default=0,validators=[MaxValueValidator(24),MinValueValidator(0)])
    sleep_time = models.FloatField(default=0,validators=[MaxValueValidator(24),MinValueValidator(0)])
    learning_time = models.FloatField(default=0,validators=[MaxValueValidator(24),MinValueValidator(0)])
    exercise_time = models.FloatField(default=0,validators=[MaxValueValidator(24),MinValueValidator(0)])
    
    @property
    def journal(self):
        return self.__journal
    
    @journal.setter
    def journal(self, value):
        self.__journal = value