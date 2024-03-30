from rest_framework import serializers
from .models import Genre, AnimeGenre, AnimeTitle

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class AnimeTitleSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = AnimeTitle
        fields = ['id', 'title', 'genres', 'description', 'release_date', 'image']