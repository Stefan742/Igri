from django.db import models

# Create your models here.
class Match(models.Model):
    sport = models.CharField(max_length=50)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    score = models.CharField(max_length=20, default="0 - 0")
    time = models.CharField(max_length=20, blank=True)
    updated_at = models.DateTimeField(auto_now=True)