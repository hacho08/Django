# Generated by Django 3.1.3 on 2024-06-09 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_auto_20240609_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
