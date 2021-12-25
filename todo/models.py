from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    check_done = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.title} {self.content}"
