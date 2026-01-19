from django.contrib import admin

from books.models import Book
from reviews.models import Review


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'price']
    list_filter = ['title', 'genre', 'price']
    search_fields = ['title', 'genre', 'price']

@admin.register(Review)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['author', 'body', 'book']
    list_filter = ['author', 'body', 'book']
    search_fields = ['author', 'body', 'book']
