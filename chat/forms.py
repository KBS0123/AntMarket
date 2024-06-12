# chat/forms.py

from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['room_name', 'image']  # 메시지 필드를 제거하고 이미지 필드만 남김
        widgets = {
            'room_name': forms.HiddenInput(),  # 방 이름을 숨김 필드로 설정
        }
