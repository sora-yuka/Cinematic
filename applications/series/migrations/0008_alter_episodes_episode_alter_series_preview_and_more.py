# Generated by Django 4.2.1 on 2023-05-13 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0007_alter_series_season_alter_series_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodes',
            name='episode',
            field=models.FileField(upload_to='series/series-episode/'),
        ),
        migrations.AlterField(
            model_name='series',
            name='preview',
            field=models.ImageField(upload_to='series/series-preview/'),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='trailer',
            field=models.FileField(upload_to='series/series-trailer/'),
        ),
    ]
