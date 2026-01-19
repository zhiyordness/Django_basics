from django.db import models

from common.models import TimeStampModel


# Create your models here.
class Review(TimeStampModel):
    author = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default='Anonymous'
    )
    body = models.TextField()
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name='book_reviews')

    def __str__(self):
        return f"{self.author} wrote: \"{self.body}\""

    class Meta:
        ordering = ['-created_at']