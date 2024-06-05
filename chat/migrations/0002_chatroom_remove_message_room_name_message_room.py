# Generated by Django 5.0.6 on 2024-06-05 00:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='room_name',
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.chatroom'),
        ),
    ]
