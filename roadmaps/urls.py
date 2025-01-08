from django.urls import path
from . import views

urlpatterns = [
    path('recommend_courses/', views.recommend_courses, name='recommend_courses'),
    path('train_ncf_model/', views.train_ncf_model, name='train_ncf_model'),
]
