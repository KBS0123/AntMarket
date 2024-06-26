# chat/urls.py

from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('list/', views.chat_list, name='list'),
    path('<str:room_name>/', views.room, name='room'),
]

