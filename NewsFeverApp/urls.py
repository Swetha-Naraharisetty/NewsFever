from django.conf.urls import url, include
from NewsFeverApp import views
from django.conf import settings
#from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    url(r'^home/$', views.home, name = 'home'),
    url(r'^home/login$', views.home, name = 'home'),
    url(r'^story$', views.story, name = 'story'),
    #url(r'^userpost$', views.userpost, name = 'userpost'),
    url(r'^signUp/$',views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^getstory/([0-9]+)$', views.getStory, name='getStory'), 
    
]
#if settings.DEBUG is True:
 #   urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

