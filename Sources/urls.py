from django.urls import path
from . import views


urlpatterns = [
    path('external_source/', views.external_source, name='external-source'),
]