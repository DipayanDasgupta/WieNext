from ollama.api import Ollama
from django.shortcuts import render
from .models import Roadmap

ollama_client = Ollama(api_key='your_ollama_api_key')

def roadmap_list(request):
    if request.method == "POST":
        user_query = request.POST.get('query')
        response = ollama_client.query(user_query)
        
        return render(request, 'roadmap_list.html', {'response': response})
    
    roadmaps = Roadmap.objects.filter(level=request.user.level)
    return render(request, 'roadmap_list.html', {'roadmaps': roadmaps})
