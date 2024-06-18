# chat/urls.py

from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    # path('', views.index, name='index'),
    path('<str:room_name>/<int:seller_id>_<int:user_id>/', views.room, name='room'),
]

