from django.contrib import admin
from .models import Album, Author, Song, Album_To_Song


admin.site.register(Album)
admin.site.register(Author)
admin.site.register(Song)
admin.site.register(Album_To_Song)