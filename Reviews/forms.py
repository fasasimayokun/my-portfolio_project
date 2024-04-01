# forms.py
from django import forms
from .models import Review, Rating

class ReviewForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Review
        fields = ['content']
        #widget = {'content': forms.TextInput(attrs={'placeholder': 'write your review'})}


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['value']