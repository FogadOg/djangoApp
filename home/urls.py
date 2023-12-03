from django.urls import path
from . import views

urlpatterns=[
    path("home/",views.index,name="home"),
    path("deleteSet/<int:setId>/", views.deleteSet, name="delete set"),
    path("logout/",views.logout,name="logout"),
]


