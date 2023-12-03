from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignupForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import login
# from .models import Profile

from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)

def delete_view(request):
    user = User.objects.get(username = request.user.username)
    user.delete()
    return redirect("/workout/bench/")


def signup(request):
    if request.user.is_authenticated==True:
        return redirect("/workout/bench/")
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/workout/bench/')
    else:
        form = SignupForm()
    return render(request, "auth/signUp.html", {'form': form})




# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()

