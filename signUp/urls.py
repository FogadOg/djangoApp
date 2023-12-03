from django.urls import path
from . import views





urlpatterns=[
    path("deleteuser/",views.delete_view,name="delete user"),
    path("signup/",views.signup,name="sign up")
]







