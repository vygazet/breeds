# Generated by Django 4.2.7 on 2023-12-06 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_images'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Images',
        ),
    ]