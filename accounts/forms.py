@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        print("FILES:", request.FILES)  # Debug print
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            profile = p_form.save(commit=False)
            if 'image' in request.FILES:
                print("New image being saved:", request.FILES['image'])  # Debug print
                profile.image = request.FILES['image']
            profile.save()
            
            messages.success(request, f'Profile updated successfully! Image path: {profile.image.url if profile.image else "No image"}')
            return redirect('profile')
        else:
            print("Form errors:", p_form.errors)  # Debug print
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'current_image_url': profile.image.url if profile.image else None  # Debug info
    }

    return render(request, 'accounts/profile.html', context)