from django.contrib import admin
from django.urls import path, include

from . import views

# path to your urls
urlpatterns = [
    path('', views.index, name='index'),
]
