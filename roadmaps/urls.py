from django.urls import path
from . import views

urlpatterns = [
    path('', views.roadmap_list, name='roadmap_list'),
]
