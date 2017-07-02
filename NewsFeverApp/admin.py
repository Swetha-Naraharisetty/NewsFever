from django.contrib import admin
from NewsFeverApp.models import Categories , SubCategory, Mapping, News, Publisher, Author, Profile
# Register your models here.
admin.site.register(Categories)
admin.site.register(SubCategory)
admin.site.register(Mapping)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(News)

#@admin.register(Categories)

