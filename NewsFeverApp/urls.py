from django.conf.urls import url, include
from NewsFeverApp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    url(r'^home/$', views.home, name = 'home'),
    url(r'^story$', views.story, name = 'story'),
    url(r'^signUp/$',views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),    

    
]
