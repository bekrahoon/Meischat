# Generated by Django 4.2.8 on 2024-09-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_myuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_received',
            field=models.BooleanField(default=False),
        ),
    ]
