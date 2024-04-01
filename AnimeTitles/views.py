from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import AnimeTitle, Genre, AnimeGenre
from .serializers import GenreSerializer, AnimeTitleSerializer
from django.template.response import TemplateResponse
from Reviews.models import Review, Rating
from Reviews.forms import ReviewForm, RatingForm
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.

def anime_reviews_list(request, anime_title_id):
    anime_title = AnimeTitle.objects.get(pk=anime_title_id)
    reviews = Review.objects.filter(anime_title=anime_title)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        rating_form = RatingForm(request.POST)
        if review_form.is_valid() and rating_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.anime_title = anime_title
            review.save()
            rating = rating_form.save(commit=False)
            rating.review = review
            rating.user = request.user
            rating.save()
            return redirect('anime-reviews-list', anime_title_id=anime_title_id)
    else:
        review_form = ReviewForm()
        rating_form = RatingForm()

    return render(request, 'anime_reviews_list.html', {'anime_title': anime_title,
                                                  'review_form': review_form,
                                                  'rating_form': rating_form,
                                                  'reviews': reviews})


def anime_reviews_update(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    # Check if the user is the author of the review
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        rating_instance = review.rating.first()  # Assuming each review has only one rating
        rating_form = RatingForm(request.POST, instance=rating_instance)
        if review_form.is_valid() and rating_form.is_valid():
            review_form.save()
            rating_form.save()
            return redirect('anime-reviews-list', anime_title_id=review.anime_title_id)  # Redirect to the review list page
    else:
        review_form = ReviewForm(instance=review)
        rating_instance = review.rating.first()  # Assuming each review has only one rating
        rating_form = RatingForm(instance=rating_instance)
    return render(request, 'anime_review_update.html', {'review_form': review_form, 'rating_form': rating_form, 'review': review})


def anime_review_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    anime_title_id = review.anime_title_id
    review.delete()
    return redirect('anime-reviews-list', anime_title_id=review.anime_title_id)

class AnimeTitleList(APIView):
    template_name = 'anime_list.html'

    def get(self, request, format=None):
        anime_titles = AnimeTitle.objects.all()
        serializer = AnimeTitleSerializer(anime_titles, many=True)
        context = {'anime_titles': serializer.data}  # Pass serialized data to template context
        return TemplateResponse(request, self.template_name, context)  # Render the template with context data
        #return Response(serializer.data)
    
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