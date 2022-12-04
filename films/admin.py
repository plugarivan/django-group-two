from django.contrib import admin
from .models import Film, Genre, Direction, Reviews

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_publ')

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'film')