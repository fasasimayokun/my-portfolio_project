from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from .forms import UserLoginForm, UserForm, ProfileForm


# Create your views here.

class WelcomeView(TemplateView):
    template_name = 'welcome.html'

def user_login(request):

    if request.method == 'POST':

        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('welcome')
            else:
                print("Someone tried to login and failed!")
                print("Username:{} and password {}".format(username, password))
                return HttpResponseBadRequest('Invalid username or password')
        else:
            pass
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)

def user_registration(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('login')
        else:
            pass
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})

