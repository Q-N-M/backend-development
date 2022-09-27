from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('home', views.emoji, name="home"),
    path('display', views.index, name="home"),
]
