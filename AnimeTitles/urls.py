from django.urls import path
from . import views
from .views import AnimeTitleList, AnimeTitleDetail, GenreList, GenreDetail, anime_reviews_list, anime_reviews_update, anime_review_delete

urlpatterns = [
    path('anime-titles/', AnimeTitleList.as_view(), name='anime-title-list'),
    path('anime-titles/<int:pk>/', AnimeTitleDetail.as_view(), name='anime-title-detail'),
    path('anime-reviews-list/<int:anime_title_id>/', anime_reviews_list, name='anime-reviews-list'),
    path('anime-reviews/<int:review_id>/update', anime_reviews_update, name='anime-reviews-update'),
    path('anime-reviews/<int:review_id>/delete', anime_review_delete, name='anime-review-delete'),
    path('genres/', GenreList.as_view(), name='genre-list'),
    path('genres/<int:pk>/', GenreDetail.as_view(), name='genre-detail'),
]