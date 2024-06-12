import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message
from django.core.files.base import ContentFile
import base64

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')
        image_data = text_data_json.get('image', '')

        if image_data:
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            image = ContentFile(base64.b64decode(imgstr), name=f'{self.room_name}_{self.channel_name}.{ext}')
        else:
            image = None

        # Save message to the database asynchronously
        new_message = await self.save_message_to_db(message, image)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'timestamp': new_message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'image_url': new_message.image.url if new_message.image else ''
            }
        )

    @database_sync_to_async
    def save_message_to_db(self, message, image):
        return Message.objects.create(
            room_name=self.room_name,
            message=message,
            image=image
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        timestamp = event['timestamp']
        image_url = event.get('image_url', '')

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'timestamp': timestamp,
            'image_url': image_url,
        }))
