from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from workoutHome.models import SetVolume
from django.urls import reverse
from django.contrib.auth import logout

def logout(request):
  logout(request)
  return redirect(reverse('login'))

def deleteSet(request, setId):
   set=SetVolume.objects.get(id=setId)
   set.delete()
   return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def index(request):
  return render(request,"index.html")







