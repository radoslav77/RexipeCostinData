from django import forms
from django.db.models import fields

from .models import *


class FileFieldForm(forms.ModelForm):
    class Meta:
        model = Exeldocument
        fields = ('doc',)
    #file_field = forms.FileField()
