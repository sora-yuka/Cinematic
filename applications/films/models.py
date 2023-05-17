from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class Genre(models.Model):
    name = models.CharField("Жанр", max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Films(models.Model):    
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    avatar = models.ImageField(upload_to='film/films_avatar/')
    film = models.FileField(upload_to='film/films_film/')
    trailer = models.FileField(upload_to='film/film_trailer')
    director = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"