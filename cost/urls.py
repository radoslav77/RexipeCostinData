from os import name
from django.contrib import admin
from django.urls import path, include

from . import views

# path to your urls
urlpatterns = [
    path('', views.index, name='index'),
    path('some_view_api', views.some_view_api, name='some_view_api'),
    path('upload', views.upload_file, name='upload_file'),
    path('recipe-upload', views.recipe_upload, name='recipe_upload'),
    path('recipe', views.recipe, name='recipe'),

    # API
    path('api_data_cost', views.api_data_cost, name='api_data_cost')
]
