#chat/urls.py
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('room/<int:market_id>/', views.market_chat_room, name='market_chat_room'),
]
