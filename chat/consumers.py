# chat/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # 채널 그룹에 사용자를 추가
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # WebSocket 연결 수락
        await self.accept()

    async def disconnect(self, close_code):
        # 채널 그룹에서 사용자를 제거
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = self.scope["user"].username  # 사용자 이름 가져오기

        # 메시지를 채팅 메시지로 전송
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username  # 메시지를 보낸 사용자 이름 전송
            }
        )

    async def chat_message(self, event):
        # 채팅 메시지를 받아서 클라이언트에 전송
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
