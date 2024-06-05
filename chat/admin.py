# chat/admin.py

from django.contrib import admin
from .models import ChatRoom, Message

admin.site.register(ChatRoom)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'content', 'timestamp')
    list_filter = ('room', 'user')