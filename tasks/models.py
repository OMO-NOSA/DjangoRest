from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=20, blank=False)
    description = models.TextField(blank=False)
    due_date = models.DateTimeField(default=datetime.now, blank=False)


    def __str__(self):
        return self.title