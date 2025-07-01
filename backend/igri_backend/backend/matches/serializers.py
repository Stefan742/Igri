from rest_framework import serializers
from .models import Match

class MatchSerializer(serializers.ModelSerializer):
    teams = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = ['id', 'sport', 'teams', 'score', 'time']

    def get_teams(self, obj):
        return f"{obj.home_team} vs {obj.away_team}"
