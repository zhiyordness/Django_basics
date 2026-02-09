from django.db import models


class GenreChoices(models.TextChoices):
    FICTION = 'Fiction', 'Fiction'
    NON_FICTION = 'Non-Fiction', 'Non-Fiction'
    FANTASY = 'Fantasy', 'Fantasy'
    SCIENCE = 'Science', 'Science'


class LanguageChoices(models.TextChoices):
    BULGARIAN = 'Bulgarian', 'Bulgarian'
    ENGLISH = 'English', 'English'
    FRENCH = 'French', 'French'
    GERMAN = 'German', 'German'
    OTHER = 'Other', 'Other'


class ReviewTypeChoices(models.TextChoices):
    TEXT = 'Text', 'Text'
    VIDEO = 'Video', 'Video'
    AUDIO = 'Audio', 'Audio'
