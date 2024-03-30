from django.contrib import admin
from .models import Genre, AnimeGenre, AnimeTitle
# Register your models here.

admin.site.register(Genre)
admin.site.register(AnimeGenre)
admin.site.register(AnimeTitle)