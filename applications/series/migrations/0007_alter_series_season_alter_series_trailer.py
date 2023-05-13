# Generated by Django 4.2.1 on 2023-05-13 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0006_alter_series_season_alter_series_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='season',
            field=models.ManyToManyField(blank=True, to='series.season', verbose_name='сезоны'),
        ),
        migrations.AlterField(
            model_name='series',
            name='trailer',
            field=models.ManyToManyField(blank=True, to='series.trailer', verbose_name='трейлеры'),
        ),
    ]
