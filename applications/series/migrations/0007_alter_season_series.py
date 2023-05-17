# Generated by Django 4.2.1 on 2023-05-17 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0006_alter_season_release_alter_season_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='season_series', to='series.series'),
            preserve_default=False,
        ),
    ]
