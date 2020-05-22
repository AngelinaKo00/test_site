from django.contrib import admin
from news.models import Articles, Post
# Register your models here.
admin.sites.site.register(Articles)
admin.site.register(Post)
