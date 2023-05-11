from django.db import models


class Films(models.Model):

    GENRE = (
        ('adventure', 'adventure'),
        ('horror', 'horror'),
        ('fantastic', 'fantastic'),
        ('romance', 'romance'),
        ('drama', 'drama'),
        ('action', 'action'),
    )
    
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE)
    avatar = models.ImageField(upload_to='films_avatar/', null=True, blank=True)
    film = models.FileField(upload_to='films_film/')
    director = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    upload_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title