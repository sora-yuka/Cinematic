from django.db import models
from applications.films.models import Films
from applications.series.models import Series
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from functools import partial

User = get_user_model()

def get_default_series():
    return Series.objects.first()

class Like(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    films = models.ForeignKey(
        Films,
        on_delete=models.CASCADE,
        related_name='likes',
        null=True
    )
    series = models.ForeignKey(
        Series,
        on_delete=models.CASCADE,
        related_name='likes',
        null=True
    )
    is_like = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.owner} liked - {self.films} liked - {self.series}'


class Rating(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    films = models.ForeignKey(
        Films,
        on_delete=models.CASCADE,
        related_name='ratings',
        null=True
    )
    series = models.ForeignKey(
        Series,
        on_delete=models.CASCADE,
        related_name='ratings',
        null=True
    )
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.owner} - {self.films.title}'


class Favorite(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites'
    )
    films = models.ForeignKey(
        Films,
        on_delete=models.CASCADE,
        related_name='favorites',
        null=True
    )
    series = models.ForeignKey(
        Series,
        on_delete=models.CASCADE,
        related_name='favorites',
        null=True
    )

    def __str__(self):
        return f'{self.owner} - {self.films.title}'


class Comment(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    films = models.ForeignKey(
        Films,
        on_delete=models.CASCADE,
        related_name='comments',
        null=True
    )
    series = models.ForeignKey(
        Series,
        on_delete=models.CASCADE,
        related_name='comments',
        null=True
    )
    comment = models.TextField()

    def __str__(self):
        return f'{self.owner} - {self.films.title}'