# Generated by Django 4.2.1 on 2023-05-15 21:24

import applications.feedback.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
        ('series', '0001_initial'),
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='series',
            field=models.ForeignKey(default=applications.feedback.models.get_default_series, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='series.series'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='series',
            field=models.ForeignKey(default=applications.feedback.models.get_default_series, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='series.series'),
        ),
        migrations.AddField(
            model_name='like',
            name='series',
            field=models.ForeignKey(default=applications.feedback.models.get_default_series, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='series.series'),
        ),
        migrations.AddField(
            model_name='rating',
            name='series',
            field=models.ForeignKey(default=applications.feedback.models.get_default_series, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='series.series'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='films',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='films.films'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='films',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='films.films'),
        ),
        migrations.AlterField(
            model_name='like',
            name='films',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='films.films'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='films',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='films.films'),
        ),
    ]
