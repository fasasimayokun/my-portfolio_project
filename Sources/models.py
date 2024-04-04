from django.db import models

class ExternalUser(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class ExternalAnimeTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class ExternalSource(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

class ExternalReview(models.Model):
    source = models.ForeignKey(ExternalSource, on_delete=models.CASCADE)
    external_title = models.ForeignKey(ExternalAnimeTitle, on_delete=models.CASCADE, null=True, blank=True)
    review_text = models.TextField()
    external_user = models.ForeignKey(ExternalUser, on_delete=models.CASCADE, null=True)
    #rating = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"Review for {self.external_title} from {self.source.name} by {self.external_user}"