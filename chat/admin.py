# chat/admin.py
from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'message', 'timestamp')
    search_fields = ('room_name', 'message')

admin.site.register(Message, MessageAdmin)




