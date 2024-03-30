from django.db import models
from django.contrib.auth.models import User
from AnimeTitles.models import AnimeTitle
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime_title = models.ForeignKey(AnimeTitle, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.anime_title}"
