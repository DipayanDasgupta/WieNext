from django.urls import path
from . import views

urlpatterns = [
    path('roadmaps/', views.RoadmapListAPI.as_view(), name='roadmap_list_api'),
]
