from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)

    task = models.TextField()

    is_completed = models.BooleanField()

    def __str__(self):
        return f"{self.title} - {self.task} - is completed: {self.is_completed}"