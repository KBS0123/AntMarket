# Generated by Django 5.0.6 on 2024-06-14 01:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0012_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minicategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='minicategories', to='market.category'),
        ),
    ]
