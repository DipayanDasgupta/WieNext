from django.db import models

class Roadmap(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tutorial_link = models.URLField()
    level = models.CharField(max_length=50)
