# Generated by Django 4.2.1 on 2023-05-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_alter_season_release_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='release_year',
            field=models.IntegerField(),
        ),
    ]
