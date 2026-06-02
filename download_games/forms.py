from django import forms
from . import models

class GameForm(forms.ModelForm):
    class Meta:
        model = models.Games
        fields = '__all__'
