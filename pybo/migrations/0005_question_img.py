# Generated by Django 3.1.3 on 2024-06-09 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0004_auto_20240609_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
