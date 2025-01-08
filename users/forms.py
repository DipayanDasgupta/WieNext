from django import forms

class OnboardingForm(forms.Form):
    question_1 = forms.CharField(label="Do you have prior experience in coding?")
    question_2 = forms.IntegerField(label="Rate your proficiency in Python (1-10):")
