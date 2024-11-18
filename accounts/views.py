from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .forms import RegistrationForm
from .models import Profile
from django.db import IntegrityError


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            try:
                Profile.objects.create(user=user, bio='')
            except IntegrityError:
                # Profile already exists, skip creation
                pass
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/profile.html', context)


def about(request):
    return render(request, 'about.html')


def fia_page(request):
    verdicts = Verdict.objects.all()

    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = IncidentForm()

    context = {
        'verdicts': verdicts,
        'form': form,
    }

    return render(request, 'fia_page.html', context)


def login_view(request):
    # After successful login
    messages.success(request, 'You have successfully logged in.')
    return redirect('home')


def logout_view(request):
    # After successful logout
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')
