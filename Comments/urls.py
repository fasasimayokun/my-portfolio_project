from django.urls import path
from .views import CommentAPIView

urlpatterns = [
    path('comments/', CommentAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentAPIView.as_view(), name='comment-detail'),
]