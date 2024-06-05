# chat/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ChatRoom(models.Model):
    # 채팅방에 대한 필드 추가 (예: 이름, 생성일 등)
    name = models.CharField(default=None, max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=255, default='')
    timestamp = models.DateTimeField(default=timezone.now)
