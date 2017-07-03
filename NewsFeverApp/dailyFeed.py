from urllib.request import urlopen
import urllib
import json

from NewsFeverApp.models import Categories , SubCategory, Mapping, News, Publisher, Author, Profile


def test_trail():
	print("hello swetha ")

def getCategory(catVal):
	category = Categories.objects.filter(category = catVal)
	for c in category:
		return c

def getSource(sourceVal):
	source = Publisher.objects.filter(p_name = sourceVal)
	for s in source:
		return s

"""     categ = Categories(category = 'Sports', c_id = 'C0001')
	categ.save()
	subCategory = SubCategory(category = 'Cricket', s_id = 'S0001')
	subCategory.save()
	mapp = Mapping(m_id = 'M0001', category = categ, sub_category = subCategory)
	mapp.save()

"""


def cricNews(source, category):
	url = "https://newsapi.org/v1/articles?source=" +source+ "&sortBy=top&apiKey=70ecac24214846759b5ca1eb23c25329"
	req = urllib.request.Request(url)
	res = urllib.request.urlopen(req)
	news_res = res.read().decode('utf-8')
	news_dict = json.loads(news_res)
	news_keys = news_dict.keys()
	articles = news_dict['articles']
	num_of_stories = len(articles)
	story_keys = articles[0].keys()
	auth = Author.objects.all()
	authLen = len(auth)
	for i in range(0, num_of_stories):
		key = 'A'
		j = '{0:04d}'.format(authLen + i)
		key += str(j)
		author = Author(a_id = key,a_name =articles[i]['author']  )
		author.save()
		news = News(author_id = author, publisher_id = getSource(news_dict['source']),title = articles[i]['title'], story = articles[i]['description'], image_url = articles[i]['urlToImage'], more_info = articles[i]['url'], public = 1, published_date = articles[i]['publishedAt'], category = getCategory(category))
		news.save()


cricNews()

		

	
	
