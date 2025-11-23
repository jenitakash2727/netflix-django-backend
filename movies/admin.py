from django.contrib import admin
from .models import Genre, Movie, Watchlist

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'release_date', 'rating']
    filter_horizontal = ['genre']
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'language', 'description', 'genre')  # ADD 'language' HERE
        }),
        ('Media', {
            'fields': ('poster', 'trailer_url', 'video_file')
        }),
        ('Details', {
            'fields': ('release_date', 'duration', 'rating')
        }),
    )
@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'added_at']