from django.db import models

STATUS = (
    ("Продолжается", "Продолжается"),
    ("Завершен", "Завершен"),
    ("Заброшен", "Заброшен"),
    ("Анонсировано", "Анонсировано"),
)


class Genre(models.Model):
    name = models.CharField("Жанр", max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        
    
class Episodes(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=180)
    episode = models.FileField(upload_to="series/series-episode/")
    
    def __str__(self) -> str:
        return self.title
    
    
    class Meta:
        verbose_name = "Серия"
        verbose_name_plural = "Серии"
        
        
class Trailer(models.Model):
    title = models.CharField(max_length=100)
    trailer = models.FileField(upload_to="series/series-trailer/")
    
    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = "Трейлер"
        verbose_name_plural = "Трейлеры"
        

class Season(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_year = models.PositiveIntegerField()
    episodes = models.ManyToManyField(Episodes, verbose_name="серии")
    
    def __str__(self) -> str:
        return self.title
    
    
    class Meta:
        verbose_name = "Сезон"
        verbose_name_plural = "Сезоны"
    
    
class Series(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    status = models.CharField(max_length=100, choices=STATUS)
    preview = models.ImageField(upload_to="series/series-preview/")
    season = models.ManyToManyField(Season, verbose_name="сезоны", blank=True)
    trailer = models.ManyToManyField(Trailer, verbose_name="трейлеры", blank=True)
    director = models.CharField(max_length=100)
    description = models.TextField()
    upload_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    
    class Meta:
        verbose_name = "Сериал"
        verbose_name_plural = "Сериалы"