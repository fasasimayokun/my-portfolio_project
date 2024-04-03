from django import forms
from .models import Review, Rating

class ReviewForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your review here...'})
    )
    
    class Meta:
        model = Review
        fields = ['content']


class RatingForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 6)],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    class Meta:from django import forms
from .models import Review, Rating

class ReviewForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control chat-input', 'placeholder': 'Write your review here...'})
    )
    
    class Meta:
        model = Review
        fields = ['content']


class RatingForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 6)],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    class Meta:
        model = Rating
        fields = ['rating']
        model = Rating
        fields = ['rating']