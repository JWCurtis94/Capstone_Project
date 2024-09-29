from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Race, RaceResult, Verdict
from .forms import RaceResultForm, IncidentTicketForm
from django.db.models import Sum, F, Case, When, IntegerField
from django.utils import timezone
from . import views
from django.contrib.auth.decorators import login_required

def home(request):
    upcoming_races = Race.objects.filter(date__gte=timezone.now()).order_by('date')[:5]
    return render(request, 'core/home.html', {'upcoming_races': upcoming_races})

@login_required
def submit_result(request):
    if request.method == 'POST':
        form = RaceResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.driver = request.user
            result.save()
            return redirect('standings')
        else:
            return render(request, 'core/submit_result.html', {'form': form, 'error': 'Invalid data'})  # Added error handling
    else:
        form = RaceResultForm()
    return render(request, 'core/submit_result.html', {'form': form})

def standings(request):
    results = RaceResult.objects.values('driver__username').annotate(
        total_points=Sum(Case(
            When(position=1, then=25),
            When(position=2, then=21),
            When(position=3, then=18),
            When(position=4, then=15),
            When(position=5, then=12),
            When(position=6, then=10),
            When(position=7, then=8),
            When(position=8, then=6),
            When(position=9, then=4),
            When(position=10, then=3),
            When(position=11, then=2),
            When(position=12, then=1),
            default=0,
            output_field=IntegerField()
        )) + Sum(
            Case(
                When(fastest_lap=True, then=1),
                default=0,
                output_field=IntegerField()
            )
        )
    ).order_by('-total_points')
    
    return render(request, 'core/standings.html', {'standings': results})

def fia(request):
    return render(request, 'core/fia.html')

def about(request):
    return render(request, 'accounts/about.html')

def fia_view(request):
    verdicts = Verdict.objects.all()
    if request.method == 'POST':
        form = IncidentTicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core/fia')
    else:
        form = IncidentTicketForm()
    
    return render(request, 'core/fia.html', {'verdicts': verdicts, 'form': form})

def calendar(request):
    upcoming_races = Race.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'core/calendar.html', {'upcoming_races': upcoming_races})

@login_required
def reaction_game(request):
    return render(request, 'reaction_game.html')