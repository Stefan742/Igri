from django.db import models

# Create your models here.
class Match(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('active', 'Active'),
        ('finished', 'Finished'),
    ]

    sport = models.CharField(max_length=50)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    score = models.CharField(max_length=20, default="0 - 0")
    time = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    scheduled_time = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

class News(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
