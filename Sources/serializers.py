from rest_framework import serializers
from .models import Source, ExternalReview

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'

class ExternalReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalReview
        fields = '__all__'