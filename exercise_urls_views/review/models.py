from django.db import models

from destination.models import Destination

# Create your models here.
class Review(models.Model):
    author = models.CharField(
        max_length=100,
    )
    body = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    destination = models.ForeignKey('destination.Destination',
                                    on_delete=models.CASCADE,
                                    related_name='reviews')
    is_published = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return f"{self.author} - {self.body}"