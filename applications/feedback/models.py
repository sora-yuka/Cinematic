from django.db import models
from applications.films.models import Films
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()

class Like(models.Model):
    
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name='likes'
    )

    films = models.ForeignKey(
        Films,
        on_delete=models.CASCADE, related_name='likes'
    )

    is_like = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.owner} liked - {self.films.title}'


class Rating(models.Model):

    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, related_name='ratings'
    ) 
    films = models.ForeignKey(
        Films, 
        on_delete=models.CASCADE, related_name='ratings'
    )
    rating = models.SmallIntegerField(
        validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
        ],
        blank=True, null=True
    )

    def __str__(self):
        return f'{self.owner} - {self.films.title}'

class Favorite(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name='favorites'
    )
    films = models.ForeignKey(
        Films, 
        on_delete=models.CASCADE, related_name='favorites'
    )

    def __str__(self):
        return f'{self.owner} - {self.films.title}'
    

class Comment(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name='comments'
    )
    films = models.ForeignKey(
        Films,
        on_delete=models.CASCADE, related_name='comments'
    )
    comment = models.TextField()
   
    def __str__(self):
        return f'{self.owner} - {self.films.title}'

