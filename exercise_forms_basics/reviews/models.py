from django.db import models

from books.models import Book
from choices import ReviewTypeChoices


class Review(models.Model):
    author = models.CharField(
        max_length=255
    )
    body = models.TextField()
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )
    is_verified = models.BooleanField(
        default=False
    )
    review_type = models.CharField(
        choices=ReviewTypeChoices.choices
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    book = models.ForeignKey(
        'books.Book',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Review by {self.author} for {self.book.title}'