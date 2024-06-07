# Generated by Django 5.0.6 on 2024-06-07 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_alter_category_slug_alter_minicategory_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]