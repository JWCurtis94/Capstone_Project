from django import forms
from .models import RaceResult, IncidentTicket
from .models import Race

class RaceResultForm(forms.ModelForm):
    class Meta:
        model = RaceResult
        fields = ['race', 'position', 'fastest_lap']

class IncidentTicketForm(forms.ModelForm):
    class Meta:
        model = IncidentTicket
        fields = ['username', 'email', 'race_name', 'incident_description']
        
class RaceForm(forms.ModelForm):
    class Meta:
        model = Race
        fields = ['name', 'date', 'track', 'sprint']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'track': forms.TextInput(attrs={'class': 'form-control'}),
            'sprint': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }