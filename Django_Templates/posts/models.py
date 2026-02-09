from django.db import models
from posts.choices import LanguageChoice
from posts.validators import BadLanguageValidator


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=50,
    )
    image = models.ImageField(
        max_length=500,
        upload_to='post_images/',
        blank=True,
        null=True,
    )
    description = models.TextField(
        validators=[
            BadLanguageValidator("This text contains bad words!")
        ]
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    author = models.CharField(
        max_length=50
    )
    language = models.CharField(
        choices=LanguageChoice.choices,
        default=LanguageChoice.OTHER
    )


class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.CharField(
        max_length=100,
    )
    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )