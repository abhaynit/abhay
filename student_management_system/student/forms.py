from django import forms
from django.db.models.base import Model
from .models import student 

class imageform(forms.ModelForm):
    class Meta:
        model = student
        fields="__all__"


class imageform1(forms.ModelForm):
    class Meta:
        model = student
        fields= ["image"]

