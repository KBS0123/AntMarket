# Generated by Django 5.0.6 on 2024-06-20 02:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0016_remove_message_product'),
        ('market', '0017_remove_product_address_remove_product_zipcode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.product'),
        ),
    ]
