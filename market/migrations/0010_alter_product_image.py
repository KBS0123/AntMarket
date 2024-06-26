from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_delete_market'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/'),
        ),
    ]
