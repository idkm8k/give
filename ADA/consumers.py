import json
from channels.generic.websocket import AsyncWebsocketConsumer
import random
import asyncio

class CompetitiveConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.random_time = random.randint(5, 25)  # simulate opponent solving
        asyncio.create_task(self.opponent_timer())

    async def opponent_timer(self):
        await asyncio.sleep(self.random_time)
        await self.send(text_data=json.dumps({
            'message': 'You lost! Opponent solved it first.',
            'status': 'lost'
        }))
        await self.close()

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get('answer'):
            # Stop opponent timer if player answers
            await self.send(text_data=json.dumps({
                'message': 'You answered!',
                'status': 'answered'
            }))
            await self.close()
