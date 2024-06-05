# chat/views.py

from django.shortcuts import render
from .models import Message, ChatRoom

def room(request, room_name):
    room = ChatRoom.objects.get(name=room_name)
    messages = room.messages.order_by('timestamp')
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages
    })

def popup(request, room_name):
    room = ChatRoom.objects.get(name=room_name)
    messages = room.messages.order_by('timestamp')
    return render(request, 'chat/popup.html', {
        'room_name': room_name,
        'messages': messages
    })
