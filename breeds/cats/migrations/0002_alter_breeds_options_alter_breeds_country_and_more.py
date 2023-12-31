# Generated by Django 4.2.7 on 2023-12-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='breeds',
            options={'ordering': ['name', 'country'], 'verbose_name': 'Veislė', 'verbose_name_plural': 'Veislės'},
        ),
        migrations.AlterField(
            model_name='breeds',
            name='country',
            field=models.CharField(max_length=100, verbose_name='Šalis'),
        ),
        migrations.AlterField(
            model_name='breeds',
            name='description',
            field=models.TextField(blank=True, verbose_name='Aprašymas'),
        ),
        migrations.AlterField(
            model_name='breeds',
            name='height',
            field=models.CharField(max_length=20, verbose_name='Maksimalus ūgis'),
        ),
        migrations.AlterField(
            model_name='breeds',
            name='lifespan',
            field=models.CharField(max_length=5, verbose_name='Gyvenimo trukmė'),
        ),
        migrations.AlterField(
            model_name='breeds',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Pavadinimas'),
        ),
    ]
