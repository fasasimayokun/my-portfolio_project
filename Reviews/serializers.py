from rest_framework import serializers
from .models import Review, Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'review', 'user', 'value']


class ReviewSerializer(serializers.ModelSerializer):
    rating = RatingSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'author', 'anime_title', 'content', 'created_at', 'updated_at', 'rating']