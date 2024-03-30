from django.urls import path
from . import views
from .views import AnimeTitleList, AnimeTitleDetail, GenreList, GenreDetail

urlpatterns = [
    path('anime-titles/', AnimeTitleList.as_view(), name='anime-title-list'),
    path('anime-titles/<int:pk>/', AnimeTitleDetail.as_view(), name='anime-title-detail'),
    path('animelist/', views.anime_list, name='animelist'),
    path('genres/', GenreList.as_view(), name='genre-list'),
    path('genres/<int:pk>/', GenreDetail.as_view(), name='genre-detail'),
]