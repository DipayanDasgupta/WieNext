from django.shortcuts import render, redirect
from .forms import OnboardingForm
from .ai_onboarding import evaluate_user_level

def onboarding_view(request):
    if request.method == "POST":
        form = OnboardingForm(request.POST)
        if form.is_valid():
            user_level = evaluate_user_level(form.cleaned_data)
            request.user.level = user_level
            request.user.save()
            return redirect('dashboard')
    else:
        form = OnboardingForm()
    return render(request, 'onboarding.html', {'form': form})

def dashboard_view(request):
    return render(request, 'dashboard.html', {'level': request.user.level})
