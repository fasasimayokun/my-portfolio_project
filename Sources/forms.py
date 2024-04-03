# forms.py
from django import forms

class AnimeSearchForm(forms.Form):
    anime_title = forms.CharField(max_length=100, label='Enter Anime Title')
