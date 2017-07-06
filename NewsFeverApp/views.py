from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from NewsFeverApp.forms import SignUpForm, CommentForm

# Create your views here.
from NewsFeverApp.models import Categories, News, Profile, Story
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
def preferences(request):
    news = News.objects.all()
    title = request.POST.get('current_news.title')
    for index in news:
        news = index
        break
    context = {'news' : news, 'title' : title}
    return render(request,'NewsFeverApp/stories.html', context)

def userpost(request):
    if request.method == 'POST':
        savenews = CommentForm(request.POST, request.FILES)
        if savenews.is_valid():
            savenews.save() 
            savenew = Story.objects.all( )
            return render(request,'NewsFeverApp/myprofile.html',{'savenews':savenew})
    else:
        form = CommentForm()
    return render(request, 'NewsFeverApp/userpost.html', {
        'form': form
    })

def getStory(request, title):
    print(title)
    #news_title = title.replace("-"," ")
    news = News.objects.filter(id = title)
    for c in news:
        news = c
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
            return render(request, 'NewsFeverApp/userprofile.html', {'user' : user})
    else:
        form = SignUpForm()
    return render(request, 'NewsFeverApp/signup.html', {'form': form})
def myprofile(request):
    details = Story.objects.all()
    return render(request, 'NewsFeverApp/myprofile.html', {'details' : details})
def home(request):
    news = News.objects.all()[5:]
    print("Calling home")
    return render(request, 'NewsFeverApp/home.html', {'news' : news})
def userprofile(request):
    news = News.objects.all()[5:]
    print("Calling home")
    return render(request, 'NewsFeverApp/userprofile.html', {'news' : news})
def business(request):
    business_news = News.objects.all()
    return render(request, 'NewsFeverApp/business.html', {'business_news' : business_news})
def entertainment(request):
    entertainment_news = News.objects.all()
    return render(request, 'NewsFeverApp/entertainment.html', {'entertainment_news' : entertainment_news})
def gaming(request):
    gaming_news = News.objects.all()
    return render(request, 'NewsFeverApp/gaming.html', {'gaming_news' : gaming_news})
def general(request):
    general_news = News.objects.all()
    return render(request, 'NewsFeverApp/general.html', {'general_news' : general_news})
def music(request):
    music_news = News.objects.all()
    return render(request, 'NewsFeverApp/music.html', {'music_news' : music_news})
def politics(request):
    politics_news = News.objects.all()
    return render(request, 'NewsFeverApp/politics.html', {'politics_news' : politics_news})       
def sports(request):
    sports_news = News.objects.all()
    return render(request, 'NewsFeverApp/sports.html', {'sports_news' : sports_news}) 
def scienceandnature(request):
    scienceandnature_news = News.objects.all()
    return render(request, 'NewsFeverApp/scienceandnature.html', {'scienceandnature_news' : scienceandnature_news})
def technology(request):
    technology_news = News.objects.all()
    return render(request, 'NewsFeverApp/technology.html', {'technology_news' : technology_news})
#def userpost(request):
    
    
