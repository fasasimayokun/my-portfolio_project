from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import ExternalAnimeTitle, ExternalReview, ExternalSource

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

def reviews_by_anime_title(request):
    anime_title = request.GET.get('anime-title')
    sources = ExternalSource.objects.all()
    try:
        if anime_title:
            reviews = ExternalReview.objects.filter(external_title__title__icontains=anime_title)
        else:
            reviews = ExternalReview.objects.all()
        
        if reviews:
            return render(request, 'external_source_reviews.html', {'reviews': reviews, 'sources': sources})
        else:
            print("There are no reviews available for the provided anime title.")
            return render(request, 'external_source_reviews.html', {'reviews': []})
    except ExternalReview.DoesNotExist:
        print("This anime doesn't have any external review at the moment")
    