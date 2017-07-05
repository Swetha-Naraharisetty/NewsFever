from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from NewsFeverApp.forms import SignUpForm

# Create your views here.
from NewsFeverApp.models import Categories, News
from NewsFeverApp.dailyFeed import getCategory
def index(request):
    category = Categories.objects.all()
    return render(request, 'NewsFeverApp/categories.html', {'categories': category})

def story(request):
    news = News.objects.all()
    for index in news:
        news = index
        break
    return render(request,'NewsFeverApp/stories.html', {'news':news})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('NewsFeverApp/home.html')
    else:
        form = SignUpForm()
    return render(request, 'NewsFeverApp/signup.html', {'form': form})

def home(request):
	newsCategory = getCategory('Gaming')

	return render(request, 'NewsFeverApp/home.html', {'news' : newsCategory})
		




