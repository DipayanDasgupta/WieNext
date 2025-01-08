from django.shortcuts import render
from .video_recommendation import fetch_recommended_videos

def roadmap_detail(request, level):
    videos = fetch_recommended_videos(f"{level} programming tutorials")
    return render(request, 'roadmap_detail.html', {'videos': videos})
