from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Match
from .serializers import MatchSerializer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    @action(detail=True, methods=['post'])
    def update_score(self, request, pk=None):
        try:
            match = self.get_object()
            score = request.data.get('score')
            time = request.data.get('time')

            if score is not None:
                match.score = score
            if time is not None:
                match.time = time

            match.save()

            # Realtime emit
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"results_{match.sport}",
                {
                    "type": "send_score",
                    "match_id": match.id,
                    "score": match.score,
                    "time": match.time,
                }
            )

            return Response(self.get_serializer(match).data)

        except Exception as e:
            print("Error in update_score:", e)
            return Response({"error": str(e)}, status=500)
