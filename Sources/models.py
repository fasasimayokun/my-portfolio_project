from django.db import models
from AnimeTitles.models import AnimeTitle
# Create your models here.

class Source(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        self.name


class ExternalReview(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    anime_title = models.ForeignKey(AnimeTitle, on_delete=models.CASCADE)
    review_text = models.TextField()
    author_name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.anime_title} from {self.source.name} by {self.author_name}"