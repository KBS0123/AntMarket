# chat/urls.py
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('<str:username>/', views.chat_view, name='chat_view'),
]
