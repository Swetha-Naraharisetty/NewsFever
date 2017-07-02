from urllib.request import urlopen
import urllib
import json
from NewsFeverApp.models import Categories , SubCategory, Mapping, News, Publisher, Author, Profile

def cricNews():
	url = "https://newsapi.org/v1/articles?source=espn-cric-info&sortBy=top&apiKey=70ecac24214846759b5ca1eb23c25329"
	req = urllib.request.Request(url)
	res = urllib.request.urlopen(req)
	news_res = res.read().decode('utf-8')
	news_dict = json.loads(news_res)
	news_keys = news_dict.keys()
	source = Publisher(p_id ='P0001',p_name = news_dict['source'])
	source.save()
	categ = Categories(category = 'Sports', c_id = 'C0001')
	categ.save()
	subCategory = SubCategory(category = 'Cricket', s_id = 'S0001')
	subCategory.save()
	mapp = Mapping(m_id = 'M0001', category = catego, sub_category = subCategory)
	mapp.save()
	articles = news_dict['articles']
	num_of_stories = len(articles)
	story_keys = articles[0].keys()
	author = Author(a_id ='A0001',a_name =articles[0]['author']  )
	author.save()
	news = News(author_id = author, publisher_id = source,title = articles[0]['title'], story = articles[0]['description'], 		image_url = articles[0]['urlToImage'], more_info = articles[0]['url'], public = 1, published_date = articles[0]['publishedAt'])


cricNews()

		

	
	
