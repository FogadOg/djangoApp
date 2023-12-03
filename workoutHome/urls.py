from django.urls import path
from . import views
from .views import HomePage

urlpatterns=[
    path("workout/<slug:exerciseName>/",HomePage.as_view(),name="workout page"),
]
