from django.core.validators import MinLengthValidator
from django.db import models

from choices import BookGenreChoices


# Create your models here.
class Book(models.Model):

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
        validators=[
            MinLengthValidator(12)
        ],
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
    slug = models.CharField(
        max_length=100,
        unique=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title