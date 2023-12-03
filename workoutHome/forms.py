from django.contrib.auth.models import User
import datetime
from django import forms  
from .models import SetVolume

class Workout(forms.Form):
    workoutName = forms.CharField(max_length=42)
    def __str__(self):
        return self.workoutName


class SetVolumeForm(forms.ModelForm):
    wight=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg mt-3','placeholder':'wight'}),label='')
    reps=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg mt-3','placeholder':'reps'}),label='')
    class Meta:
        model=SetVolume
        fields=["wight","reps"]

