from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Workout, SetVolume
from .forms import SetVolumeForm
from datetime import datetime
from django.views import View


class HomePage(View):
  def get(self, request, exerciseName):
    exerciseName=Workout.objects.get(workoutName=exerciseName)

    if request.user.is_authenticated==False:
      return redirect("signup/")
    
    form=SetVolumeForm()

    volumeData=SetVolume.objects.filter(user_id=request.user.id,exercise=exerciseName)

    # volumeData=volumeData.filter(exercise__name="bench")

    wight=[]
    reps=[]
    date=[]
    for i in volumeData:
      wight.append(i.wight)
      reps.append(i.reps)

      dateToReforamt = i.date
      reformatedDate = dateToReforamt.strftime('%Y-%m-%d')
      date.append(reformatedDate)

    
    return render(request, "service/index.html", {"workouts":Workout.objects.all, 
                "form":form,
                "username":request.user.username,
                "workoutData":volumeData,
                "workoutDataWight":wight,
                "workoutDataReps":reps,
                "workoutDataDate":date,
              })
  

  def post(self, request, exerciseName):
    exerciseName=Workout.objects.get(workoutName=exerciseName)
    print("exerciseName: ",exerciseName.workoutName)


    form=SetVolumeForm(request.POST)
    if form.is_valid():
      wight=request.POST.get("wight")
      reps=request.POST.get("reps")

      workoutForm=form.save(commit=False)

      workoutForm.wight=wight
      workoutForm.reps=reps
      workoutForm.exercise=exerciseName
      workoutForm.user=request.user

      workoutForm.save()
      return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))






