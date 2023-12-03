from django.db import models
from django.contrib.auth.models import User
import datetime

class Workout(models.Model):
    workoutName = models.CharField(max_length=42)
    def __str__(self):
        return self.workoutName


class SetVolume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    exercise = models.ForeignKey(Workout, on_delete=models.CASCADE, default=None)
    wight=models.IntegerField() 
    reps=models.IntegerField()
    date=models.DateField(default=datetime.date.today) 


    # def __str__(self):
    #     return str(self.user)+" "+str(self.wight)+"kg x "+str(self.reps)
