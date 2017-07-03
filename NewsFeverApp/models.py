from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Categories(models.Model):
	category = models.CharField(max_length = 50)
	c_id = models.CharField(primary_key = True, max_length = 4)
	
	def __str__(self):
		return self.category 

class SubCategory(models.Model):
	category = models.CharField(max_length = 50)
	s_id = models.CharField(primary_key = True, max_length = 4)

	def __str__(self):
		return self.category

class Mapping(models.Model):
	m_id = models.CharField(primary_key = True, max_length = 4)
	category = models.ForeignKey(Categories, on_delete = models.CASCADE)
	sub_category = models.ForeignKey(SubCategory, on_delete = models.CASCADE)

	def __str__(self):
		return self.category


class Publisher(models.Model):
	p_id = models.CharField(primary_key = True, max_length = 4)
	p_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.p_name

class Author(models.Model):
	a_id = models.CharField(primary_key = True,max_length = 5)
	a_name = models.CharField(max_length = 50, null = True ,default = 'Unknown')

	def __str__(self):
		return self.a_id

class News(models.Model):
	author_id = models.ForeignKey(Author, on_delete = models.CASCADE)
	publisher_id = models.ForeignKey(Publisher, on_delete = models.CASCADE)
	title = models.CharField(max_length = 100)
	story = models.CharField(max_length = 500)
	image_url = models.CharField(max_length = 100)
	more_info = models.CharField(max_length = 200)
	public = models.IntegerField(default = 1)
	published_date = models.DateTimeField(null = True,default = timezone.now)
	category = models.ForeignKey(Categories, on_delete = models.CASCADE)

	def __str__(self):
		return self.author_id

class Favourite(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	story_id = models.ForeignKey(News, on_delete = models.CASCADE)  


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
	fname = models.CharField(max_length = 100)
	mname = models.CharField(max_length = 50, null = True, blank = True, default = None)
	lname = models.CharField(max_length = 50, null = True, blank = True, default = None)
	is_self_ratting = models.BooleanField(default = False)
	is_registered = models.BooleanField(default = False)
	is_pwd_reset = models.BooleanField(default = False) 

	
