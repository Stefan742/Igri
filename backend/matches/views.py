from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.dateparse import parse_datetime
from .models import Match
from .serializers import MatchSerializer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from unidecode import unidecode
from rest_framework import status


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    @action(detail=False, methods=['get'], url_path='by-sport/(?P<sport>[^/.]+)')
    def by_sport(self, request, sport=None):
        normalized_sport = unidecode(sport).lower()
        matches = self.queryset.filter(sport__iexact=normalized_sport)
        serializer = self.get_serializer(matches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def update_score(self, request, pk=None):
        try:
            match = self.get_object()
            score = request.data.get('score')
            time = request.data.get('time')
            status = request.data.get('status')
            scheduled_time = request.data.get('scheduled_time')

            if score is not None:
                match.score = score
            if time is not None:
                match.time = time
            if status is not None:
                match.status = status
            if scheduled_time is not None:
                dt = parse_datetime(scheduled_time)
                if dt is not None:
                    match.scheduled_time = dt

            match.save()

            # Realtime emit
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"results_{unidecode(match.sport.lower())}",
                {
                    "type": "send_score",
                    "match_id": match.id,
                    "score": match.score,
                    "time": match.time,
                    "status": match.status,
                    "scheduled_time": match.scheduled_time.isoformat() if match.scheduled_time else None,
                }
            )

            return Response(self.get_serializer(match).data)

        except Exception as e:
            print("Error in update_score:", e)
            return Response({"error": str(e)}, status=500)
