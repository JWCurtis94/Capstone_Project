from django import forms
from .models import RaceResult

class RaceResultForm(forms.ModelForm):
    class Meta:
        model = RaceResult
        fields = ['race', 'position', 'fastest_lap']