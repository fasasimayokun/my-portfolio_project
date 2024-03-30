from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import AnimeTitle, Genre, AnimeGenre
from .serializers import GenreSerializer, AnimeTitleSerializer
import requests

# Create your views here.
class AnimeTitleList(APIView):
    def get(self, request, format=None):
        anime_titles = AnimeTitle.objects.all()
        serializer = AnimeTitleSerializer(anime_titles, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AnimeTitleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnimeTitleDetail(APIView):
    def get_object(self, pk):
        try:
            return AnimeTitle.objects.get(pk=pk)
        except AnimeTitle.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        anime_title = self.get_object(pk)
        serializer = AnimeTitleSerializer(anime_title)
        return serializer.data
    
    def put(self, request, pk):
        anime_title = self.get_object(pk)
        serializer = AnimeTitleSerializer(anime_title, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        anime_title = self.get_object(pk)
        anime_title.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
class GenreList(APIView):
    def get(self, request, format=None):
        anime_genres = Genre.objects.all()
        serializer = GenreSerializer(anime_genres, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GenreDetail(APIView):
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk)
        except Genre.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        genre = Genre.objects.get_object(pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)


##############
'''
def anime_list(request):
    # Make GET request to your API endpoint
    response = requests.get('http://localhost:8000/api/animetitle/anime-titles/')  # Replace with your actual API URL

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        # Pass data to template
        return render(request, 'anime_list.html', {'anime_list': data})
    else:
        # Handle error
        return render(request, 'error.html', {'error_message': 'Failed to fetch data from API'})
'''