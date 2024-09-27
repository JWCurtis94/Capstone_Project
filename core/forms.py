from django import forms
from .models import RaceResult
from .models import IncidentTicket

class RaceResultForm(forms.ModelForm):
    class Meta:
        model = RaceResult
        fields = ['race', 'position', 'fastest_lap']

class IncidentTicketForm(forms.ModelForm):
    class Meta:
        model = IncidentTicket
        fields = ['username', 'email', 'race_name', 'incident_description']
        widgets = {
            'incident_description': forms.Textarea(attrs={'rows': 5}),
        }

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'description', 'race_number']