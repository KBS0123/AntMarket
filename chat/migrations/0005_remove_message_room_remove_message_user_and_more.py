# Generated by Django 5.0.6 on 2024-06-07 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_remove_message_image_chatroom_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
