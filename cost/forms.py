from django import forms
from django.db.models import fields

from .models import *


class FileFieldForm(forms.ModelForm):
    class Meta:
        model = Exeldocument
        fields = ('title', 'doc')
    #file_field = forms.FileField()


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'recipe', 'method')
