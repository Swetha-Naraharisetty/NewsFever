from urllib.request import urlopen
import urllib
import json

from NewsFeverApp.models import Categories , SubCategory, Mapping, News, Publisher, Author, Profile, SourceCategoryMap


def test_trail():
	print("hello swetha ")

def getCategory(catVal):
	category = Categories.objects.filter(category = catVal)
	for c in category:
		return c

def getSource(sourceVal):
	source = Publisher.objects.filter(p_id = sourceVal)
	for s in source:
		return s

def getSourceId(sourceVal):
	source = Publisher.objects.filter(p_name = sourceVal)
	for s in source:
		return s.p_id

"""  
category = Categories.objects.filter(category = 'Science-and-Nature')
for c in category:
    category = c
   
for k, v in science_and_nature_publishers.items():
     src = getSource(k)	
     source = SourceCategoryMap(category = category, source = src)
     source.save()





"""
# cat= ['General', 'Business', 'Technology', 'Sports', 'Entertainment', 'Politics', 'Gaming', 'Music', 'Science-and-Nature']

#general_publishers= {'ABC News(AU)':'abc-news-au', 'Al Jazeera English':'al-jazeera-english','Associated Press':'associated-press','BBC News': 'bbc-news','Blid': 'blid','CNN': 'cnn', 'Der Tagesspiegel':'der-tagesspiegel', 'Focus':'focus', 'Google News':'google-news','Independent': 'independent','Metro': 'metro','Mirror': 'mirror', 'NewsWeek':'newsweek','New york Magazine': 'new-york-magazine','Reddit/r/all': 'reddit-r-all', 'Reuters':'reuters','Spiegel Online': 'spiegel-online', 'The Guardian (AU)':'the-guardian-au','The Guardian (UK)': 'the-guardian-uk','The Hindu': 'the-hindu','The Huffington Post': 'the-huffington-post','The New York Times': 'the-new-york-times','The Telegraph':'the-telegraph','The Times of India': 'the-times-of-india', 'The Washington Post':'the-washington-post', 'Time':'time','USA Today': 'usa-today'}

#business_publishers = {'Bloomberg':'bloomberg',  'Business Insider':'business-insider','Business Insider(UK)':'business-insider-uk', 'CNBC':'cnbc', 'Die Zeit':'die-zeit', 'Financial Times':'financial-times', 'Fortune':'fortune', 'Handelsblatt':'handelsblatt', 'The Economist':'the-economist', 'The Wall Street Journal':'the-wall-street-journal', 'Wirtschafts Woche':'wirtschafts-woche'}

#technology_publishers = {'Ars Technica':'ars-technica', 'Engadget':'engadget', 'Gruenderszene':'gruenderszene', 'Hacker News':'hacker-news', 'Recode':'recode', 'T3n':'t3n', 'TechCrunch':'techcrunch', 'TechRadar':'techradar', 'The Next Web':'the-next-web', 'The Verge':'the-verge', 'Wired de':'wired-de'}

#sports_publishers = {'BBC Sports':'bbc-sports', 'ESPN':'espn', 'ESPN Cric Info':'espn-cric-info', 'Football Italic':'football-italic', 'Four Four Two':'four-four-two', 'Fox Sports':'fox-sports', 'NFL News':'nfl-news', 'TalkSport':'talksport', 'The Sport Bible':'the-sport-bible'}

#entertainment_publishers = {'Daily Mail':'daily-mail', 'Buzzfeed':'buzzfeed', 'Mashable':'mashable', 'The Lad Bidle':'the-lab-bible', 'Entertainment Weekly':'entertainment-weekly'}

#politic_publishers = {'Breitbart News':'breitbart-news'}

#gaming_publishers = {'IGN':'ign', 'Polygon':'polygon'}

#music_publishers = {'MTV News':'mtv-news', 'MTV News(UK)':'mtv-news-uk'}

#science_and_nature_publishers = {'National Geographic':'national-geographic', 'New Scientist':'new-scientist'}

#publishers = ['general_publishers', 'business_publishers','technology_publishers','sports_publishers', 'entertainment_publishers', 'politic_publishers', 'gaming_publishers','music_publishers', 'science_and_nature_publishers']


"""
for k, v in science_and_nature_publishers.items():
...     src = getSource(k)
...     source = SourceCategoryMap(category = category, source = src)
...     source.save()

 """
def getSourceNews(source, category):
	url = "https://newsapi.org/v1/articles?source="+source+"&sortBy=top&apiKey=70ecac24214846759b5ca1eb23c25329"
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
		nullVal = None
		if(articles[i]['title'] != nullVal and articles[i]['urlToImage'] != nullVal  and articles[i]['description'] != nullVal):
			key = 'A'
			auth = Author.objects.all()
			j = '{0:09d}'.format(len(auth) + 1)
			key += str(j)
			author = Author(a_id = key,a_name =articles[i]['author']  )
			author.save()
			news = News(author_id = author, publisher_id = getSource(news_dict['source']),title = articles[i]['title'], story = articles[i]['description'], image_url = articles[i]['urlToImage'], more_info = articles[i]['url'], public = 1, published_date = articles[i]['publishedAt'], category = getCategory(category))
			news.save()
		else :
			print("Insufficient Data")

def getNews():
	src = SourceCategoryMap.objects.all()
	for index in src:
		print(getSourceId(index.source), index.category)
		getSourceNews(getSourceId(index.source), index.category)



	



		

	
	
