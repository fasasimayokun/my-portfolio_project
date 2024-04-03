from django.shortcuts import render, redirect
from django.http import JsonResponse
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from .models import Source, ExternalReview
from AnimeTitles.models import AnimeTitle
import requests


def fetch_external_reviews(anime_title):
    url = f'https://myanimelist.net/anime/{anime_title}/reviews'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        reviews = soup.find_all('div', class_='borderDark')
        for review in reviews:
            author = review.find('a', class_='hoverinfo_trigger').text.strip()
            review_content = review.find('div', class_='spaceit').text.strip()
            source = Source.objects.create(name=url)
            ExternalReview.objects.create(
                source=source,
                anime_title=anime_title,
                author_name=author,
                review_text=review_content,
                # Add other necessary fields here
            )


def external_source(request):
    anime_title = request.GET.get('anime_title')
    if anime_title:
        fetch_external_reviews(anime_title)  # Assuming this function stores reviews in the database
        reviews = ExternalReview.objects.filter(anime_title=anime_title)
        return render(request, 'eternal_source_reviews.html', {'reviews': reviews})
    return render(request, 'external_source_reviews.html')