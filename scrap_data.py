import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AnimeReviewHub.settings')

# Initialize Django
django.setup()



from django.shortcuts import render, redirect
from django.http import JsonResponse
from bs4 import BeautifulSoup

from Sources.models import ExternalAnimeTitle, ExternalReview, ExternalSource, ExternalUser
import requests



# Define the URL and User-Agent header
url = "https://myanimelist.net/reviews.php?t=anime"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Make the request with headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all review elements
    review_elements = soup.find_all('div', class_='review-element js-review-element')
    # Process or store the results
    for review_element in review_elements:
        # Extract data from each review element
        anime_title = review_element.find('div', class_='titleblock mb4').find('a').text
        created_at = review_element.find('div', class_='thumbbody mt8').find('div', class_='update_at').text
        username = review_element.find('div', class_='thumbbody mt8').find('div', class_='username').find('a').text
        content = review_element.find('div', class_='thumbbody mt8').find('div', class_='text').text.strip()

        # Create or get ExternalSource instance
        source, _ = ExternalSource.objects.get_or_create(name='MyAnimeList', website=url)

        # Create or get ExternalAnimeTitle instance
        anime_title_instance, _ = ExternalAnimeTitle.objects.get_or_create(title=anime_title)

        # Create or get ExternalUser instance
        user, _ = ExternalUser.objects.get_or_create(username=username)

        # Create ExternalReview instance and save to database
        review = ExternalReview.objects.create(
            source=source,
            external_title=anime_title_instance,
            review_text=content,
            external_user=user,
            created_at=created_at  # use the time from the external source
        )

else:
    print("Failed to retrieve data. Status code:", response.status_code)

