from django.contrib import admin


from NewsFeverApp.models import SubCategory ,Categories , Mapping, News, Publisher, Author, Profile,SourceCategoryMap, Favourite
# Register your models here.


admin.site.register(SubCategory)

admin.site.register(Categories)
admin.site.register(Mapping)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(News)
admin.site.register(Favourite) 
admin.site.register(Profile)
admin.site.register(SourceCategoryMap)

#@admin.register(mine)

