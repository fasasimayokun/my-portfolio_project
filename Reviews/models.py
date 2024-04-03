from django.db import models
from django.contrib.auth.models import User
from AnimeTitles.models import AnimeTitle
from django.utils import timezone

# Create your models here.

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    anime_title = models.ForeignKey(AnimeTitle, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review for {self.anime_title.title} by {self.author}"
    
    class Meta:
        # Add a unique constraint to ensure that there are no duplicate reviews
        unique_together = ('author', 'anime_title')

class Rating(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='rating')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])

    def __str__(self):
        return f"{self.user.username} gave {self.review.anime_title} -> {self.rating}"