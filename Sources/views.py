from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import ExternalAnimeTitle, ExternalReview, ExternalSource
from django.contrib import messages
from AnimeTitles.models import AnimeTitle

def review_list(request):
    reviews = ExternalReview.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

def review_detail(request, review_id):
    review = get_object_or_404(ExternalReview, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})

def reviews_by_source(request, source_id):
    source = get_object_or_404(ExternalSource, pk=source_id)
    reviews = ExternalReview.objects.filter(source=source)
    return render(request, 'reviews_by_source.html', {'source': source, 'reviews': reviews})

def reviews_by_filter(request):
    # Get the filter criteria from the request
    filter_criteria = request.GET.get('filter_criteria')

    # Initialize the queryset
    reviews = ExternalReview.objects.all()
    sources = ExternalSource.objects.all()

    # Apply the filter based on the selected criteria
    if filter_criteria == 'recent':
        # Filter by recent date
        reviews = reviews.order_by('-created_at')  # Most recent first
    elif filter_criteria == 'oldest':
        # Filter by old date
        reviews = reviews.order_by('created_at')   # Oldest first

    # Render the template with filtered reviews
    return render(request, 'review_source.html', {'reviews': reviews, 'sources': sources})
    
def reviews_by_anime_title(request):
    anime_title = request.GET.get('anime_title')
    filter_criteria = request.GET.get('filter_criteria')
    sources = ExternalSource.objects.all()
    try:
        if anime_title:            # Convert anime_title and titles in the database to lowercase for case-insensitive comparison
            anime_title_lower = anime_title.lower()
            reviews = ExternalReview.objects.filter(external_title__title__icontains=anime_title_lower)
            if filter_criteria == 'recent':
                reviews = reviews.order_by('-created_at')  # Most recent first
            elif filter_criteria == 'oldest':
                reviews = reviews.order_by('created_at')   # Oldest first
        else:
            reviews = ExternalReview.objects.all()
        
        if reviews:
            return render(request, 'external_source_reviews.html', {'reviews': reviews, 'sources': sources})
        else:
            messages.success(request, f"There are no reviews available for the provided anime title: {anime_title}" )
            return render(request, 'external_source_reviews.html', {'reviews': []})
    except ExternalReview.DoesNotExist:
        messages.success(request, f"Error retrieving reviews for anime title: {anime_title}")
        return render(request, 'external_source_reviews.html', {'reviews': []})
    

def autocomplete(request):
    query = request.GET.get('query', '')
    suggestions = ExternalAnimeTitle.objects.filter(title__icontains=query)[:10] # Limit suggestions to 10
    suggestions_list = [title.title for title in suggestions]
    return JsonResponse({'suggestions': suggestions_list})
    # anime_titles = AnimeTitle.objects.filter(title__icontains=query).values_list('title', flat=True)
    # return JsonResponse(list(anime_titles), safe=False)