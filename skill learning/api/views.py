from rest_framework import generics
from roadmaps.models import Roadmap
from roadmaps.serializers import RoadmapSerializer

class RoadmapListAPI(generics.ListAPIView):
    queryset = Roadmap.objects.all()
    serializer_class = RoadmapSerializer
