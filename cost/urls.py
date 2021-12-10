from django.contrib import admin
from django.urls import path, include

from . import views

# path to your urls
urlpatterns = [
    path('', views.index, name='index'),
    path('some_view_api', views.some_view_api, name='some_view_api')
]
