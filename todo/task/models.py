from django.db import models

# Create your models here.
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    date = models.DateTimeField(default=timezone.now, null=True)
    check_done = models.BooleanField()

    def __str__(self):
        return f"{self.title} + ' ' + {self.detail}"
