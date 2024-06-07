from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'market', 'message', 'timestamp')
    search_fields = ('user__username', 'message')
    list_filter = ('timestamp',)

