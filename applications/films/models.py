from django.db import models


class Genre(models.Model):
    name = models.CharField("Жанр", max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанp"
        verbose_name_plural = "Жанры"


class Films(models.Model):    
    title = models.CharField(max_length=100)
    # genre = models.CharField(max_length=100, choices=GENRE)
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    avatar = models.ImageField(upload_to='films_avatar/', null=True, blank=True)
    film = models.FileField(upload_to='films_film/')
    director = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    upload_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Филм"
        verbose_name_plural = "Филмы"
    
    