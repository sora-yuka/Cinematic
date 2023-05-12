from django.db import models


class Genre(models.Model):
    name = models.CharField("Жанр", max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        
    
class Episodes(models.Model):
    title = models.CharField(max_length=100)
    episodes = models.FileField(upload_to="series-episodes")
    
    def __str__(self) -> str:
        return self.title
    
    
class Series(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    # status = models.Choices()
    preview = models.ImageField(upload_to="series-preview/")
    series = models.ManyToManyField(Episodes, verbose_name="серии")
    director = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Сериал"
        verbose_name_plural = "Сериалы"