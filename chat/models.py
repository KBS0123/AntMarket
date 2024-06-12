# chat/models.py

from django.db import models

class Message(models.Model):
    room_name = models.CharField(max_length=255, default='default_room_name')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='chat_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.room_name} - {self.message[:50]}'
