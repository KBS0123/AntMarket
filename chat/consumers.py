# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 유저 그룹을 채팅방으로 설정 (예: "chat_방ID")
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # 채팅방 그룹에 가입
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # 채팅방 그룹에서 탈퇴
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # 웹소켓으로부터 메시지를 받음
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # 채팅방 그룹에 메시지를 보냄
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # 그룹에서 메시지를 받을 때 호출
    async def chat_message(self, event):
        message = event['message']

        # 웹소켓으로 메시지를 보냄
        await self.send(text_data=json.dumps({
            'message': message
        }))