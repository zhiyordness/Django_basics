from django.db import models
from django.utils.text import slugify

from choices import GenreChoices, LanguageChoices


class Book(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    isbn = models.CharField(
        max_length=13,
        unique=True
    )
    genre = models.CharField(
        choices=GenreChoices.choices
    )
    language = models.CharField(
        choices=LanguageChoices.choices
    )
    pages = models.PositiveIntegerField()
    is_available = models.BooleanField(
        default=True
    )
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(
        unique=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title