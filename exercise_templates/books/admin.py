from django.contrib import admin
from django.template.library import TagHelperNode

from books.models import Book, Tag
from reviews.models import Review


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'price']
    list_filter = ['title', 'genre', 'price']
    search_fields = ['title', 'genre', 'price']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...