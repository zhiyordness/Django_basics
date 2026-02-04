from django.contrib import admin

from reviews.models import Review


@admin.register(Review)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['author', 'body', 'book']
    list_filter = ['author', 'body', 'book']
    search_fields = ['author', 'body', 'book']