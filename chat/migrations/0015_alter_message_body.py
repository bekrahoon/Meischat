# Generated by Django 5.1.1 on 2024-09-29 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_remove_myuser_public_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
    ]
