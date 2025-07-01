from channels.generic.websocket import AsyncJsonWebsocketConsumer

class ScoreConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.sport = self.scope['url_route']['kwargs']['sport']
        self.group_name = f"results_{self.sport}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def send_score(self, event):
        await self.send_json({
            "match_id": event["match_id"],
            "score": event["score"],
            "time": event["time"],
        })
