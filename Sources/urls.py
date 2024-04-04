from django.urls import path
from .views import review_list, review_detail, reviews_by_source, reviews_by_anime_title

urlpatterns = [
    path('reviews/', review_list, name='review_list'),
    path('reviews/<int:review_id>/', review_detail, name='review_detail'),
    path('sources/<int:source_id>/reviews/', reviews_by_source, name='reviews_by_source'),
    path('reviews_by_anime_title/', reviews_by_anime_title, name='reviews-by-anime-title'),
]