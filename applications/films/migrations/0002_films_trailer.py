# Generated by Django 4.2.1 on 2023-05-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='trailer',
            field=models.FileField(default=1, upload_to='film_trailer'),
            preserve_default=False,
        ),
    ]