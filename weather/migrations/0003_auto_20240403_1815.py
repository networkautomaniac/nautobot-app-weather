# Generated by Django 3.2.24 on 2024-04-03 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20240314_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='wind_direction',
            field=models.CharField(default='N/A', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weather',
            name='wind_speed',
            field=models.CharField(default='N/A', max_length=255),
            preserve_default=False,
        ),
    ]
