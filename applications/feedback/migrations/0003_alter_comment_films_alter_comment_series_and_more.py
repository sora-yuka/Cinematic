# Generated by Django 4.2.1 on 2023-05-16 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
        ('series', '0001_initial'),
        ('feedback', '0002_comment_series_favorite_series_like_series_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='films',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='films.films'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='series.series'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='films',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='films.films'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='series.series'),
        ),
        migrations.AlterField(
            model_name='like',
            name='films',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='films.films'),
        ),
        migrations.AlterField(
            model_name='like',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='series.series'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='films',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='films.films'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='series.series'),
        ),
    ]
