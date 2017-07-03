from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from NewsFeverApp.models import Categories, News
def index(request):
    category = Categories.objects.all()
    return render(request, 'NewsFeverApp/categories.html', {'categories': category})

def story(request):
    news = News.objects.all()
    for index in news:
        news = index
        break
    return render(request,'NewsFeverApp/stories.html', {'news':news})
