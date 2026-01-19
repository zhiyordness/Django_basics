from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from choices import BookGenreChoices
from common.models import TimeStampModel


# Create your models here.
class Book(TimeStampModel):

    title = models.CharField(
        max_length=50,
        unique=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    isbn = models.CharField(
        max_length=12,
        unique=True,
    )
    genre = models.CharField(
        max_length=30,
        choices=BookGenreChoices.choices,
        default=BookGenreChoices.NON_FICTION
    )
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True
    )
    publisher = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.title

    def  save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title} - {self.publisher}")
        super().save(*args, **kwargs)
