from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class UserForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length='100'
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        ),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        ),
        max_length="100",
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        ),
        max_length="100",
    )

    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
     
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class ProfileForm(forms.ModelForm):

    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length='100')
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = ['profile_pic', 'location', 'bio']
        widgets = {
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
        }

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-label form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-label form-control', 'placeholder': 'Password'}))