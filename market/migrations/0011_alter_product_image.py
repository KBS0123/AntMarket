# Generated by Django 5.0.6 on 2024-06-14 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0010_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/products/%Y/%m/%d/'),
        ),
    ]
