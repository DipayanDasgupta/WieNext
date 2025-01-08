from django.urls import path
from . import views

urlpatterns = [
    path('onboarding/', views.onboarding_view, name='onboarding'),
    path('onboarding/success/', views.onboarding_success, name='onboarding_success'),
]
