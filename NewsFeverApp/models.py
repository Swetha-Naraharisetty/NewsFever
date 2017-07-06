from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import os
def get_image_path(instance,filename):
      return os.path.join(' ',filename)
class Categories(models.Model):
	category = models.CharField(max_length = 50)
	c_id = models.CharField(primary_key = True, max_length = 4)
	
	def __str__(self):
		return self.category

class SubCategory(models.Model):
	category = models.CharField(max_length = 50)
	s_id = models.CharField(primary_key = True, max_length = 4)

	def __str__(self):
		return self.s_id

class Mapping(models.Model):
	m_id = models.CharField(primary_key = True, max_length = 4)
	category = models.ForeignKey(Categories, on_delete = models.CASCADE)
	sub_category = models.ForeignKey(SubCategory, on_delete = models.CASCADE)

	def __str__(self):
		return self.m_id


class Publisher(models.Model):
	p_id = models.CharField(primary_key = True, max_length = 50)
	p_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.p_name
class SourceCategoryMap(models.Model):
	category = models.ForeignKey(Categories, on_delete = models.CASCADE)
	source = models.OneToOneField(Publisher, on_delete = models.CASCADE)
	def __str__(self):
		return "{0}  {1}".format( self.source, self.category)
class Author(models.Model):
	a_id = models.CharField(primary_key = True,max_length = 10)
	a_name = models.CharField(max_length = 50, null = True ,default = 'Unknown')

	def __str__(self):
		return self.a_name

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
		return self.story

class Favourite(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	story_id = models.ForeignKey(News, on_delete = models.CASCADE)  


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
	fname = models.CharField(max_length = 100)
	mname = models.CharField(max_length = 50, null = True, blank = True, default = None)
	lname = models.CharField(max_length = 50, null = True, blank = True, default = None)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	is_self_ratting = models.BooleanField(default = False)
	is_registered = models.BooleanField(default = False)
	is_pwd_reset = models.BooleanField(default = False) 


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
	    Profile.objects.create(user=instance)
    instance.profile.save()
    
class Story(models.Model):
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length=255,)
    category = models.CharField(max_length = 255,)
    image = models.FileField(upload_to = get_image_path, blank = True,null = True)
    def __str__(self):
        return self.title

	
