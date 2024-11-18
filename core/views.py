from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Race, RaceResult, Verdict, IncidentTicket, ReactionTime
from .forms import RaceResultForm, IncidentTicketForm, RaceForm
from django.db.models import Sum, F, Case, When, IntegerField
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages


def home(request):
    upcoming_races = Race.objects.filter(
        date__gte=timezone.now()
    ).order_by('date')[:5]
    return render(
        request, 'core/home.html', {'upcoming_races': upcoming_races}
    )


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
            return render(
                request, 'core/submit_result.html',
                {'form': form, 'error': 'Invalid data'}
            )
    else:
        form = RaceResultForm()
    return render(request, 'core/submit_result.html', {'form': form})


def standings(request):
    upcoming_races = Race.objects.all().order_by('date')
    return render(request, 'core/standings.html', {'upcoming_races': upcoming_races})

    return render(request, 'core/standings.html', {
        'standings': results,
        'upcoming_races': upcoming_races
    })

    return render(
        request, 
        'core/standings.html', 
        {'standings': results, 'upcoming_races': upcoming_races}
    )


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

    return render(
        request, 'core/fia.html', {'verdicts': verdicts, 'form': form}
    )


def calendar(request):
    upcoming_races = Race.objects.filter(
        date__gte=timezone.now()
    ).order_by('date')
    return render(
        request, 'core/calendar.html', {'upcoming_races': upcoming_races}
    )


@login_required
def reaction_game(request):
    return render(request, 'reaction_game.html')


def live_stream(request):
    return render(request, 'core/live_stream.html')

class RaceListView(ListView):
    model = Race
    template_name = 'race_list.html'
    context_object_name = 'races'
    ordering = ['date']

# Update an existing race
class RaceCreateView(CreateView):
    model = Race
    form_class = RaceForm
    template_name = 'core/race_form.html'
    success_url = reverse_lazy('standings')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Race {form.instance.name} added successfully')
        return response

class RaceUpdateView(UpdateView):
    model = Race
    form_class = RaceForm
    template_name = 'core/race_form.html'
    success_url = reverse_lazy('standings')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Race {form.instance.name} updated successfully')
        return response

class RaceDeleteView(DeleteView):
    model = Race
    template_name = 'core/race_confirm_delete.html'
    success_url = reverse_lazy('standings')
    
    def delete(self, request, *args, **kwargs):
        race = self.get_object()
        messages.success(request, f'Race {race.name} deleted successfully')
        return super().delete(request, *args, **kwargs)