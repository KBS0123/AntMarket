# Generated by Django 5.0.6 on 2024-06-20 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0015_remove_message_receiver_alter_message_room_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='product',
        ),
    ]
