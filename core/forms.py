from django import forms
from .models import RaceResult, IncidentTicket

class RaceResultForm(forms.ModelForm):
    class Meta:
        model = RaceResult
        fields = ['race', 'position', 'fastest_lap']

class IncidentTicketForm(forms.ModelForm):
    class Meta:
        model = IncidentTicket
        fields = ['username', 'email', 'race_name', 'incident_description']