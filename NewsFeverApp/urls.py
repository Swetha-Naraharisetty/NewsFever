from django.conf.urls import url, include
from NewsFeverApp import views
from django.conf import settings
#from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    url(r'^home/$', views.home, name = 'home'),
    url(r'^home/login$', views.userprofile, name = 'userprofile'),
    url(r'^home/logout$', views.home, name = 'home'),
    url(r'^home/story$', views.story, name = 'story'),
    url(r'^myprofile$', views.myprofile, name = 'myprofile'),
    url(r'^userpost$', views.userpost, name = 'userpost'),
    url(r'^signUp/$',views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^getstory/([0-9]+)$', views.getStory, name='getStory'), 
    url(r'^business/$', views.business, name='business'), 
    url(r'^general/$', views.general, name='general'), 
    url(r'^entertainment/$', views.entertainment, name='entertainment'),
    url(r'^gaming/$', views.gaming, name='gaming'),
    url(r'^music/$', views.music, name='music'),
    url(r'^politics/$', views.politics, name='politics'),
    url(r'^sports/$', views.sports, name='sports'),
    url(r'^science_and_nature/$', views.scienceandnature, name='science_and_nature'),
    url(r'^technology/$', views.technology, name='technology'), 
    url(r'^preferences$', views.preferences, name = 'preferences'),
    
]
#if settings.DEBUG is True:
 #   urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

