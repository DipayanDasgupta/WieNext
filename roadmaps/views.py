from django.shortcuts import render
from .models import Roadmap

def roadmap_list(request):
    roadmaps = Roadmap.objects.filter(level=request.user.level)
    return render(request, 'roadmap_list.html', {'roadmaps': roadmaps})
