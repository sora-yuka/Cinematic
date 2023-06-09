# Generated by Django 4.2.1 on 2023-05-17 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('avatar', models.ImageField(upload_to='film/films_avatar/')),
                ('film', models.FileField(upload_to='film/films_film/')),
                ('trailer', models.FileField(upload_to='film/film_trailer')),
                ('director', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
                ('genres', models.ManyToManyField(to='films.genre', verbose_name='жанры')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Films',
            },
        ),
    ]
