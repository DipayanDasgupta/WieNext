from django import forms
from .models import UserProfile

class OnboardingForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['onboarding_completed']
        widgets = {
            'onboarding_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
