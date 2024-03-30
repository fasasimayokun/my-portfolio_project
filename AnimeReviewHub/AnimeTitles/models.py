from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class AnimeTitle(models.Model):
    title = models.CharField(max_length=50)
    genres = models.ManyToManyField(Genre, through='AnimeGenre')
    description = models.TextField()
    release_date = models.DateField()
    image = models.ImageField(upload_to='anime_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    

class AnimeGenre(models.Model):
    anime_title = models.ForeignKey(AnimeTitle, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.anime_title.title} - {self.genre.name} ({self.count})"