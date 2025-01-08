from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('roadmaps/', include('roadmaps.urls')),
    path('api/', include('api.urls')),  # Placeholder for future API endpoints
]
